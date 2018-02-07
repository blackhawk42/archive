import shutil
import sys
import os
import os.path
import getopt

# Help building
shortopts = 'ztgbxh'
longopts = ('zip', 'tar', 'gz', 'bz2', 'xz', 'help')
avaiable_formats = shutil.get_archive_formats()

USAGE_STRING = 'Usage: {} [options] DIR1 [DIRN...]\nOptions:\n'.format(sys.argv[0])

for s, l in zip(shortopts, longopts):
	USAGE_STRING += '   -{}, --{}\n'.format(s,l)

USAGE_STRING += '\nAvaiable formats on this system:\n'

for form, desc in avaiable_formats:
	USAGE_STRING += '  {:10}{}\n'.format(form + ':', desc)

if __name__ == '__main__':
	
	# Opts
	try:
		opts, args = getopt.gnu_getopt(sys.argv[1:], shortopts, longopts)
	except getopt.GetoptError as e:
		print(e.msg, file=sys.stdout)
		print(USAGE_STRING, file=sys.stderr)
		sys.exit(2)
	# Possible algos: zip, tar, gztar, bztar, xztar
	archive_format = 'zip'
	for opt, arg in opts:
		if opt in ('-z', '--zip'):
			archive_format = 'zip'
		elif opt in ('-t', '--tar'):
			archive_format = 'tar'
		elif opt in ('-g', '--gz'):
			archive_format = 'gztar'
		elif opt in ('-b', '--bz2'):
			archive_format = 'bztar'
		elif opt in ('-x', '--xz'):
			archive_format = 'xztar'
		elif opt in ('-h', '--help'):
			print(USAGE_STRING, file=sys.stderr)
			sys.exit(0)
	
	# Checking if format is valid
	invalid_format = True
	for form, desc in avaiable_formats:
		if form == archive_format:
			invalid_format = False
	
	if invalid_format:
		print('error: invalid format', file=sys.stderr)
		print(USAGE_STRING, file=sys.stderr)
		sys.exit(3)
	
	# Archiving
	for filename in args:
		if not os.path.isdir(filename):
			print('File "{}" is not an existing directory'.format(filename),
					file=sys.stderr)
		else:
			shutil.make_archive(os.path.basename(filename),
								archive_format,
								root_dir = os.path.dirname(os.path.abspath(filename)),
								base_dir = os.path.basename(filename) )

			
