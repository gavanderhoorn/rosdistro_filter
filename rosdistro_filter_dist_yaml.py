#!/usr/bin/env python

import os
import yaml
import argparse
import sys



parser = argparse.ArgumentParser()
parser.add_argument('distro_yaml')
parser.add_argument('repos', nargs='*', type=str, help='Repository entries to keep.')
args = parser.parse_args()

with open(args.distro_yaml, 'r') as f:
    content = yaml.load(f)

# these are repositories, not packages
whitelist = args.repos

sys.stderr.write('Keeping: {}\n'.format(', '.join(whitelist)))

to_remove = set(content['repositories'].keys()) - set(whitelist)

for key in to_remove:
    del content['repositories'][unwanted_key]

sys.stdout.write(yaml.safe_dump(content, default_flow_style=False))
