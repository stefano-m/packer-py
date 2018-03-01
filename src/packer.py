#!/usr/bin/env python3

# Write Hashicorp Packer templates using YAML!
#
# Copyright (C) 2018 Stefano Mazzucco <stefano AT curso DOT re>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import json
import subprocess
import sys
import yaml

from tempfile import NamedTemporaryFile

__version__ = 'development'  # The Makefile injects the version from git here.

PACKER_COMMANDS = ('build', 'fix', 'inspect', 'validate', 'version')


def make_parser():
    parser = argparse.ArgumentParser(
        description='A wrapper around packer that uses YAML templates.',
        epilog='''
        Copyright (C) 2018  Stefano Mazzucco.
        This program comes with ABSOLUTELY NO WARRANTY.
        This is free software, and you are welcome to redistribute it
        under certain conditions (https://www.gnu.org/licenses/gpl-3.0.txt).
        '''
    )
    parser.add_argument(
        '--version',
        help='The version  of this wrapper',
        action='version',
        version=__version__
    )
    parser.add_argument(
        'command',
        help='Packer command.',
        type=str,
        choices=PACKER_COMMANDS,
    )
    parser.add_argument(
        'yaml_template',
        help='Packer template in YAML format.',
        nargs='?',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        'other',
        help='Other Packer options.',
        nargs=argparse.REMAINDER,
        type=str,
    )
    return parser


def main(args):

    command = args.command
    options = args.other
    yaml_template = args.yaml_template

    if yaml_template is None:
        return run_packer([command] + options)

    try:
        data = yaml.safe_load(yaml_template)
    finally:
        yaml_template.close()

    with NamedTemporaryFile(
            mode='w+',
            prefix='packer-',
            suffix='.json') as json_template:
        json.dump(data, json_template)
        json_template.seek(0)

        packer_args = [command] + options + [json_template.name]

        if command == 'fix':
            proc = run_packer(packer_args,
                              stdout=subprocess.PIPE)
            out = yaml.safe_load(proc.stdout)
            yaml.safe_dump(out, stream=sys.stdout, default_flow_style=False)
            return proc
        else:
            return run_packer(packer_args)


def run_packer(args, **kwargs):
    default_kwargs = {
        'bufsize': 0,
        'stdout': sys.stdout,
        'stderr': sys.stderr
    }
    default_kwargs.update(kwargs)

    return subprocess.run(
        ['packer'] + args,
        **default_kwargs
    )


def run():
    parser = make_parser()
    args = parser.parse_args()
    proc = main(args)
    sys.exit(proc.returncode)


if __name__ == '__main__':
    run()
