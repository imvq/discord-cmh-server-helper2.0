from collections import namedtuple


# String representations for the bot's commands.
class Commands:
    PING = '!ping'
    INFO = '!info'
    DIE = '!die'


# String representations for the bot's parametrized commands.
class ParamCommands:
    _schema = namedtuple('ParamsCommand', ['command', 'params'])
    SWITCH_LANG = _schema._make([
        '!lang', ('--en-us', '--ru-ru', )
    ])
