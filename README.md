# jinstall: automated file installer

## What it jinstall?

**jinstall** is an automated text-based file installer. It is the perfect tool
for easily installing your dotfiles!

From a repository of files (typically put under version control) and according
to rules (described in `Jinstall` files), **jinstall** creates links to those
files where you want them to be.

**jinstall** was primarily designed to automate the process of installing
*dotfiles*, but it can be used for anything that requires installing files.

See the demo below of **jinstall** in action when installing my configuration
files for bash. The folder where I keep all my dotfiles is `~/etc`.

![jinstall demo](docs/demo.gif)

## Installation

    # python setup.py install

Or there is also a [package](https://aur.archlinux.org/packages/jinstall-git)
for ArchLinux.

You will also need to install [pdmenu](https://joeyh.name/code/pdmenu/), which
is used for the text-based UI.

## Usage

**jinstall** is a text-based program meant to be used in a terminal. Without
any arguments, it will try to read a `Jinstall` in the current directory.
Otherwise you can specify the path of a directory as argument: `jinstall
[path]`

    $ jinstall -h
    usage: jinstall [-h] [-p] [dir]

    positional arguments:
      dir           Start from a specific directory instead of the current one

    optional arguments:
      -h, --help    show this help message and exit
      -p, --pdmenu  Only generate a string for feeding pdmenu

Note that the `-p` is for internal use (the program calls itself recursively to
generate submenus).

Once in the menus, you can move with the up and down arrows, go in a submenu
using [enter] or go back from a submenu using [escape].

In a submenu, a file can be prefixed with two characters:

* `*` if the file is already installed
* `%` if the link for this file is already installed but does not point to this
  file

Typing [enter] when encountering those files will ask you if you want the
current link to be overwritten (`ln -i`).

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

## Example

Let's say your dotfile folder contains two subfolders, for bash and vim
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

At the root of your dotfile folder, create a third `Jinstall` file to inform
**jinstall** about the two subfolders:

    $ cat Jinstall
    rdir:bash
    rdir:vim

And voilà! Now, you can run **jinstall** and install your dotfiles easily!

# Mirrors

This project is mirrored on:
* [github](https://github.com/joel-porquet/jinstall)
* [my cgit](https://joel.porquet.org/cgit/cgit.cgi/jinstall.git/about/).
