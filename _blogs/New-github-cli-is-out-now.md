---
layout: blogs
permalink: /blogs/how-to-use-github-cli
title: How to use Github Newly released CLI
img_path: /static/images/blogs/GitHubCLI_SocialCard_VersionNumber_NoSubLine_v2.png
meta_desc: how to use github cli ?? GitHub CLI. gh is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with git and your code. GitHub CLI brings GitHub to your terminal. It reduces context switching, helps you focus, and enables you to more easily script and create your own workflows.
description: GitHub CLI. gh is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with git and your code. GitHub CLI brings GitHub to your terminal. It reduces context switching, helps you focus, and enables you to more easily script and create your own workflows.
tag1: github
tag2: cli
---

# Table of contents
- [Table of contents](#table-of-contents)
- [GitHub CLI](#github-cli)
- [Installation](#installation)
  - [macOS](#macos)
      - [Homebrew](#homebrew)
      - [MacPorts](#macports)
  - [Linux](#linux)
  - [Windows](#windows)
    - [scoop](#scoop)
    - [Chocolatey](#chocolatey)
- [Authentication](#authentication)
- [USAGE](#usage)
  - [Core Commands](#core-commands)
  - [Additional Commands](#additional-commands)
  - [Flags](#flags)


# GitHub CLI

`gh` is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with `git` and your code.

![screenshot of gh pr status](https://user-images.githubusercontent.com/98482/84171218-327e7a80-aa40-11ea-8cd1-5177fc2d0e72.png)

# Installation

##  macOS

`gh` is available via Homebrew and MacPorts.

#### Homebrew

|Install:|Upgrade:|
|---|---|
|`brew install gh`|`brew upgrade gh`|

#### MacPorts

|Install:|Upgrade:|
|---|---|
|`sudo port install gh`|`sudo port selfupdate && sudo port upgrade gh`|



## Linux

Install:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
sudo apt-add-repository https://cli.github.com/packages
sudo apt update
sudo apt install gh
```

**Note**: most systems will have `apt-add-repository` already. If you get a _command not found_
error, try running `sudo apt install software-properties-common` and trying these steps again.

Upgrade:

```bash
sudo apt update
sudo apt install gh
```


## Windows

`gh` is available via **scoop**, **Chocolatey**

### scoop

Install:

```powershell
scoop bucket add github-gh https://github.com/cli/scoop-gh.git
scoop install gh
```

Upgrade:

```powershell
scoop update gh
```

### Chocolatey

|Install:|Upgrade:|
|---|---|
|`choco install gh`|`choco upgrade gh`|


# Authentication

Run `gh auth login` to authenticate with your GitHub account

# USAGE
```
gh <command> <subcommand> [flags]
```

## Core Commands

[`gist`](https://cli.github.com/manual/gh_gist) :       Create gists

[`issue`](https://cli.github.com/manual/gh_issue) :      Manage issues

[`pr`](https://cli.github.com/manual/gh_pr) :         Manage pull requests

[`release`](https://cli.github.com/manual/gh_release) :    Manage GitHub releases

[`repo`](https://cli.github.com/manual/gh_repo) :       Create, clone, fork, and view repositories


## Additional Commands

[`alias`](https://cli.github.com/manual/gh_alias):      Create command shortcuts

[`api`](https://cli.github.com/manual/gh_api):        Make an authenticated GitHub API request

[`auth`](https://cli.github.com/manual/gh_auth):       Login, logout, and refresh your authentication

[`completion`](https://cli.github.com/manual/gh_completion): Generate shell completion scripts

[`config`](https://cli.github.com/manual/gh_config):     Manage configuration for gh

`help`:       Help about any command


## Flags 

`--help `:    Show help for command

`--version`:   Show gh version


Read the manual at [https://cli.github.com/manual/](https://cli.github.com/manual/)