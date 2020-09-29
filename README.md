# My Portfolio Website

This is a portfolio website created using jekyll.

Go and see in action https://rahulmanoj.xyz

If you want to take this to your local machine for testing or development, You can do the following:

> 📢 **PSA for those who want to fork or copy this repo and use it for their own site:**
>
> If You like this website and want to make your's, You can surely do that !!
> Please be a decent person and give me proper credit by linking back to my website! 
> 


## Prerequisites

- [Ruby](https://www.ruby-lang.org/en/downloads/) version **2.5.0** or higher, including all development headers (check your Ruby version using `ruby -v`)
- [RubyGems](https://rubygems.org/pages/download) (check your Gems version using `gem -v`)
- [GCC](https://gcc.gnu.org/install/) and [Make](https://www.gnu.org/software/make/) (check versions using `gcc -v`, `g++ -v`, and `make -v`)
  
If the above mentioned requirements are satisfied, Now you are ready to install jekyll !!

## Install Jekyll

`gem install jekyll bundler`


Once it is installed successfully you are ready to test my portfolio locally and make changes

## Instructions

- `git clone https://github.com/rawho/portfolio-jekyll.git`

- once it is cloned move in to the correct directory by `cd portfolio-jekyll`

- Then lets install all the bundles by `bundle install`
- This sometimes shows some error, then you have to do `bundle update`
- once it is done, you can type `bundle exec jekyll serve`
- This will create a server at port 4000, You can visit http://localhost:4000, there you can see the website.

If you like this jekyll and want to know more [click here](https://jekyllrb.com/docs/)


## Writing blogs

To write blogs create a file with extension md, inside `_blogs` folder

You have to add some metadata to this file

```
---
layout: blogs
permalink: /blogs/create-anything-you-like/
title: Create anything you like
img_path: /static/images/blogs/feynman.png
description: Here are a big list of links you can go through inorder to build any thing you think. !!
meta_desc: Here are a big list of links you can go through inorder to build any thing you think. !!
tag1: create
tag2: anything
display: f
---
```
**After this metadata you can write your content in [markdown](https://gist.github.com/cuonggt/9b7d08a597b167299f0d) syntax**

Lets take a look at it,
Since this site is highly Search Engine Optimised, you have to give meta_desc here. 
- **layout**: This is the layout you can see in `_layouts` folder
- **permalink**: This will be you url to see that blog
- **img_path**: This will be the thumbnail to your blog
- **meta_desc**: This will be sent as the desc of meta tag. Give a better desc, this will determine the google index, so while writing research about meta keywords, for better SEO
- **display**: for this you have 2 options - `t` or `f`
    - if you give `t`, Then it will be displayed in the Home page
    - if you give `f`, Then it will be displayed when you go to see all blogs (ie http://localhost/blogs)