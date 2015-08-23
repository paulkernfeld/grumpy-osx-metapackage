Grumpy OSX Metapackage
======================
Grumpy OSX Metapackage is a brutally minimal meta package installer for OSX. It lets you install dependencies from many different package managers in a single place. This might be useful in setting up or migrating configuration between developer workstations. It's not particularly friendly, though.

Usage
-----
Create a JSON file specifying which packages you want. See `pauls_packages.json` for an example.

Execute `./grumpy_osx_metapackage.py install my_packages.json` to install all packages. Grumpy OSX Metapackage uses Homebrew as the basis for installing everything else, so it will first attempt to bootstrap Homebrew if it doesn't find it.

Grumpy OSX metapackage is idempotent, so you can edit `my_packages.json` and re-run the script. It does not upgrade or uninstall packages.

