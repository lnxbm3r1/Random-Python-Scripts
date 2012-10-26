#!/usr/bin/python

import sys
import re
import os
import urllib2
import commands

def yt_url_parse(user): # parsing rss
	rssf = urllib2.urlopen('http://gdata.youtube.com/feeds/base/users/%s/newsubscriptionvideos' % (user))
	url = re.findall(r'link.+(http://www.youtube.com/watch\?v=...........)', rssf.read())
	return url

def main():
	args = sys.argv[1:]
	if not args or len(args) > 2:
		print 'Usage: ytsubdl.py [user] [directory]'
		sys.exit(1)
	os.chdir(args[1])
	url = yt_url_parse(args[0])
	print 'Downloading your subscriptions (last 20 videos)'
	for video in url:
		cmd = "/usr/local/bin/youtube-dl -o '%(upload_date)s-%(uploader)s-%(stitle)s.%(ext)s' "
		print 'Downloading ' + video
		cmd = cmd + '\'%s\'' % video
		print commands.getoutput(cmd)
	print 'Videos downloaded'
	return

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print 'Interrupted by user'
		pass

# basov