#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Serge Rey'
SITENAME = u'Serge Rey'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = 'feeds/%s.atom.xml'
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = 'feeds/%s.atom.xml'

# Blogroll
LINKS = (('PySAL', 'http://pysal.readthedocs.org/en/latest/'),
         ('GeoDa Center', 'http://geodacenter.asu.edu/'),
         )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/sergerey'),
                    ('github', 'http://github.com/sjsrey'),)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-bootstrap3"

DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU = False

FAVICON = 'images/favicon.png'

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

#CATEGORY_FEED = 'feeds/%s.atom.xml'
#FEED = 'feeds/all.atom.xml'
#TAG_FEED = 'feeds/%s.atom.xml'
