=========================================
packer-py: write Packer templates in YAML
=========================================

`Packer <https://www.packer.io>` is a nice tool, but its configuration files
are written in JSON. That means that editing the files by hand is somewhat
cumbersome (with all those quotes and whatnot).

This is a simple wrapper script that allows one to use the YAML format to write
`Packer templates <https://www.packer.io/docs/templates/>`.  Simply run the
script and pass the usual `Packer commands
<https://www.packer.io/docs/commands/>` and options, but instead of a JSON
template, pass a YAML one.

Note that when the ``fix`` command is run, the script will convert the JSON
output from packer into YAML for you.

Installation
------------

At the moment this project in not on PyPI, but you have several options to use
it:

* simply copy the script over on your machine, make it executable and run
  it. You are responsible of installing its dependencies though!

* clone this repository, run `make egg`, make the ``egg`` file in the ``dist``
  directory executable and copy it somewhere in your ``$PATH``. You are
  responsible of installing its dependencies though!

* use ``pip install`` by doing either of the below:

  * clone this repository and run ``pip install .`` (you may or may not want to
    use a virtual environment). The script will be available as ``packer-py``.

  * use ``pip``'s `VCS support
    <https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support>`

