# -*- coding: utf-8
from __future__ import unicode_literals

import os
import re

from optparse import OptionParser, OptionError, OptionGroup


GLOBAL_OPTIONS = [
    '--debug',
    '--endpoint-url',
    '--no-verify-ssl',
    '--no-paginate',
    '--output',
    '--profile',
    '--region',
    '--version',
    '--color',
    '--query',
    '--no-sign-request',
]

RESOURCE_OPTIONS = [
    '--instance-ids',
    '--bucket',
]

IAWS_COMMANDS = [
    'aws',
    'docs',
]

def all_commands():
    p = os.path.dirname(os.path.realpath(__file__))
    f = os.path.join(p, 'data/SOURCES.txt')
    commands = []
    sub_commands = []
    COMMANDS_INDEX = 2
    SUB_COMMANDS_INDEX = 3
    with open(f) as fp:
        for line in fp:
            if 'awscli/examples/' in line:
                line = re.sub('.rst\n', '', line)
                tokens = line.split('/')
                commands.append(tokens[COMMANDS_INDEX])
                sub_commands.append(tokens[SUB_COMMANDS_INDEX])
    return sorted(list(commands)), sorted(list(sub_commands))