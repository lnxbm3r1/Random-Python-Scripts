#!/usr/bin/python

import sys, os, time

def backup(db, bdir): # actual backup process
	cmd = 'pg_dump %s | gzip -c > %s/%s.%s.gz' % (db, bdir, time.strftime(format('%d.%m')), db) # dumping postgres database to gzip, saving into day.month.gz file
	os.system(cmd)
	clean(bdir)
	return

def clean(bdir): # cleaning up old (>2 weeks) backups
	lbdir = os.listdir(bdir)
	os.chdir(bdir)
	if len(lbdir) == 0:
		for b in lbdir:
			print b
		print 'This directory is empty.'
		sys.exit(0)
	for b in lbdir:
		if time.time() - os.path.getmtime(b) > 1209600:
			os.remove(b)
			print 'Removing %s, since it\'s older than 2 weeks.' % (b)
		else:
			print '%s is less than 2 weeks old, keeping it.' % (b)
	sys.exit(0)
	return

def main():
	args = sys.argv[1:]
	if not args or len(args) > 2:
		print 'Usage: pgbackup.py [db][backupdir] or --clean [backupdir]'
		sys.exit(0)
	elif args[0] == '--clean': # going straight to clean func
		clean(args[1])

	backup(args[0], args[1])
	return

if __name__ == '__main__':
	main()

# basov