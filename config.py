import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }

})
c.url.searchengines = {
    'DEFAULT':  'https://google.com/search?hl=en&q={}',
    '!a':       'https://www.amazon.com/s?k={}',
    '!d':       'https://duckduckgo.com/?ia=web&q={}',
    '!dd':      'https://thefreedictionary.com/{}',
    '!e':       'https://www.ebay.com/sch/i.html?_nkw={}',
    '!fb':      'https://www.facebook.com/s.php?q={}',
    '!gh':      'https://github.com/search?o=desc&q={}&s=stars',
    '!gist':    'https://gist.github.com/search?q={}',
    '!gi':      'https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1',
    '!gn':      'https://news.google.com/search?q={}',
    '!ig':      'https://www.instagram.com/explore/tags/{}',
    '!m':       'https://www.google.com/maps/search/{}',
    '!p':       'https://pry.sh/{}',
    '!r':       'https://www.reddit.com/search?q={}',
    '!sd':      'https://slickdeals.net/newsearch.php?q={}&searcharea=deals&searchin=first',
    '!t':       'https://www.thesaurus.com/browse/{}',
    '!tw':      'https://twitter.com/search?q={}',
    '!w':       'https://en.wikipedia.org/wiki/{}',
    '!yelp':    'https://www.yelp.com/search?find_desc={}',
    '!yt':      'https://www.youtube.com/results?search_query={}'
}

# Fonts
c.fonts.tabs.selected = "11pt Fira Mono" 
c.fonts.tabs.unselected = "11pt Fira Mono"
c.fonts.hints = "bold 15px Fira Mono"
c.fonts.completion.entry = "10pt Fira Mono"
c.fonts.completion.category = "bold 10pt Fira Mono"
c.fonts.debug_console = "10pt Fira Mono"
c.fonts.downloads = "10pt Fira Mono"
c.fonts.hints = "bold 13px Fira Mono"
c.fonts.keyhint = "10pt Fira Mono"
c.fonts.messages.error = "10pt Fira Mono"
c.fonts.messages.info = "10pt Fira Mono"
c.fonts.messages.warning = "10pt Fira Mono"
c.fonts.prompts = "10pt Fira Sans"
c.fonts.statusbar = "10pt Fira Mono"
c.fonts.web.family.fixed = "Fira Mono"
c.fonts.web.family.sans_serif = "Fira Sans"
c.fonts.web.family.serif = "DejaVu Serif"
