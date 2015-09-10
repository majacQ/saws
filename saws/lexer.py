# -*- coding: utf-8
from pygments.lexer import RegexLexer
from pygments.lexer import words
from pygments.token import Keyword, Name, Operator, Generic, Literal
from .commands import AWS_COMMAND, AWS_DOCS, generate_all_commands, \
    CommandType
from .config import read_configuration, get_shortcuts


class CommandLexer(RegexLexer):

    config = read_configuration()
    shortcuts = get_shortcuts(config)
    shortcut_tokens = []
    for shortcut in shortcuts.keys():
        tokens = shortcut.split()
        for token in tokens:
            shortcut_tokens.append(token)
    commands = generate_all_commands()
    tokens = {
        'root': [
            (words(tuple(AWS_COMMAND),
                   prefix=r'\b',
                   suffix=r'\b'),
             Literal.String),
            (words(tuple(AWS_DOCS),
                   prefix=r'\b',
                   suffix=r'\b'),
             Literal.Number),
            (words(tuple(commands[CommandType.COMMANDS.value]),
                   prefix=r'\b',
                   suffix=r'\b'),
             Name.Class),
            (words(tuple(commands[CommandType.SUB_COMMANDS.value]),
                   prefix=r'\b',
                   suffix=r'\b'),
             Keyword.Declaration),
            (words(tuple(commands[CommandType.GLOBAL_OPTIONS.value]),
                   prefix=r'',
                   suffix=r'\b'),
             Generic.Output),
            (words(tuple(commands[CommandType.RESOURCE_OPTIONS.value]),
                   prefix=r'',
                   suffix=r'\b'),
             Operator.Word),
            (words(tuple(shortcut_tokens),
                   prefix=r'',
                   suffix=r'\b'),
             Name.Exception),
        ]
    }