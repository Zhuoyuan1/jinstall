# jinstall: automated file installer

## What it jinstall?

**jinstall** is an automated terminal-based file installer. It is the perfect
tool for easily installing your *dotfiles*!

From a repository of files (typically put under version control) and according
to rules (described in `Jinstall` files), **jinstall** creates links to those
files where you want them to be.

**jinstall** was primarily designed to automate the process of installing
*dotfiles*, but it can be used for anything that requires installing files.

## Installation

    # ./setup.py install

Or there is also a [package](https://aur.archlinux.org/packages/jinstall-git)
for ArchLinux.

## Usage

**jinstall** is a terminal-based program. Without any arguments, it will try to
read a `Jinstall` in the current directory.  Otherwise you can specify the path
of a directory as argument: `jinstall [path]`

    $ jinstall -h
    usage: jinstall [-h] [-d level] [dir]

    positional arguments:
      dir           Start from a specific directory instead of the current one

    optional arguments:
      -h, --help    show this help message and exit
      -d {0,1,2}, --debug {0,1,2}  increase output debugging

Once in the menus, you can move with the up and down arrows, go in a submenu
using [enter] or go back from a submenu using [escape].

For installing or uninstalling a specific file, press [space].

## Jinstall file syntax

As of today, a `Jinstall` file contains two types of rules: `rdir` and `link`.

### rdir

The rule `rdir` (*recurse directory*) tells **jinstall** to generate a submenu
for the specified directory. Such directory must contain a `Jinstall` file.

    rdir:<directory_path>

### link

The rule `link` informs **jinstall** to create a symbolic link between a
specific file in the current directory and an absolute target.

    link:<relative_local_filepath>:<absolute_link_target>

There can be multiple `link` rules to the same link target. In this case,
Jinstall will display radiobuttons for choosing which version you want to
install.

## Example

Let's say your *dotfile* folder contains two subfolders, for bash and vim
configurations.

    $ tree
    bash
    ├── bash_aliases
    ├── bash_profile
    └── bashrc
    vim
    ├── colors
    │   └── light.vim
    ├── gvimrc
    └── vimrc

Create two `Jinstall` in both subfolders, specifying the links that have to be
created:

    $ cat bash/Jinstall
    link:bash_aliases:~/.bash_aliases
    link:bash_profile:~/.bash_profile
    link:bashrc:~/.bashrc

    $ cat vim/Jinstall
    link:colors:~/.vim/colors
    link:gvimrc:~/.gvimrc
    link:vimrc:~/.vimrc

At the root of your *dotfile* folder, create a third `Jinstall` file to inform
**jinstall** about the two subfolders:

    $ cat Jinstall
    rdir:bash
    rdir:vim

And voilà! Now, you can run **jinstall** and install your *dotfiles* easily!

# Mirrors

This project is mirrored on:

* [github](https://github.com/joel-porquet/jinstall)
* [my cgit](https://joel.porquet.org/cgit/cgit.cgi/jinstall.git/about/)
