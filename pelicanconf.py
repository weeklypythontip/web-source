from __future__ import unicode_literals

AUTHOR = u'Moshe Zadka'
SITENAME = u'Weekly Python Tip'
SITEURL = 'https://weeklypythontip.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ("Moshe'z", 'https://moshez.wordpress.com/'),
         ("Python", 'https://python.org/'),
         ("Python documentation", 'https://www.python.org/doc/'),
         ("Planet Python", 'http://planetpython.org/'),
        )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

ABOUT_ME = """
Check out our <a href="https://www.facebook.com/weeklypythontip/">Facebook Page</a>.
Every week, we post a Python tip -- a technique, a third-party package
or a standard library module.
Follow us, and improve your Python-fu!
"""
