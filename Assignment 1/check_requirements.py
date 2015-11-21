import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict
import argparse
# dependencies can be any iterable with strings, 
# e.g. file line-by-line iterator
"""
dependencies = [
  'Werkzeug>=0.6.1',
  'Flask>=0.9',
]
"""
# here, if a dependency is not met, a DistributionNotFound or VersionConflict
# exception is thrown. 
def check_presence(filename):
	dependencies = []
	with open(filename) as fp:
		for line in fp.readline():
			dependencies.append(line[:-1])
	pkg_resources.require(dependencies)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	print args.filename
	check_presence(args.filename)