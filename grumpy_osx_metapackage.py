#!/usr/bin/env python
import json
from os.path import dirname, join, realpath
from subprocess import check_call
from sys import argv


def _print_and_run(command, **kwargs):
    print " ".join(command)
    check_call(command, **kwargs)
    print


def install_packages(commands, all_packages):
    # Update Homebrew or bootstrap it if it's not present
    _print_and_run(
            ['brew update || ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'],
            shell=True
    )

    # Loop over every package in every category
    for command_name, packages in all_packages.viewitems():
        for package in packages:

            # Substitute the actual package name for the word "package"
            command = commands[command_name]
            insert_index = command.index("package")
            final_command = command[:insert_index] + [package] + command[insert_index+1:]

            # Print the command and run it!
            _print_and_run(final_command)


if __name__ == "__main__":
    if argv[1] != "install":
        raise ValueError('Usage: grumpy_osx_metapackage.py install {my_packages.json}')

    # Load the commands and packages to install
    script_dir = dirname(realpath(__file__))
    commands = json.load(open(join(script_dir, "commands.json")))
    all_packages = json.load(open(argv[2]))

    install_packages(commands, all_packages)
