#!/usr/bin/env python
from subprocess import check_call
from sys import argv
import yaml


def install_packages(packages_yml_path):
    # Update Homebrew or bootstrap it if it's not present
    check_call(['brew update || ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'], shell=True)
    print

    # Load the commands and packages to install
    commands = yaml.load(open("commands.yml"))
    all_packages = yaml.load(open(packages_yml_path))

    # Loop over every package in every category
    for category in all_packages:
        ((command_name, packages),) = category.items()
        for package in packages:

	    # Substitute the actual package name for the word "package"
	    command = commands[command_name]
	    insert_index = command.index("package")
            final_command = command[:insert_index] + [package] + command[insert_index+1:]

	    # Print the command and run it!
            print " ".join(final_command)
            check_call(final_command)
            print

if __name__ == "__main__":
    if argv[1] != "install":
	raise ValueError('The first argument must be, "install"')

    install_packages(argv[2])
