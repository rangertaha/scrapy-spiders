# -*- coding: utf-8 -*-

# Scrapy settings for rss project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rss'

SPIDER_MODULES = ['rss.spiders']
NEWSPIDER_MODULE = 'rss.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rss (+http://www.yourdomain.com)'


LOG_ENABLED = True
LOG_FILE = 'rss.log'

ITEM_PIPELINES = {
    'rss.pipelines.RssPipeline': 0,
}