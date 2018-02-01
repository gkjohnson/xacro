import os
from os import path

def resolve_args(str, context, resolve_anon):
    str = str[2:-1]
    op = str.split(' ')[0]
    arg = str.split(' ')[1]

    if (op == 'find'):
        origpath = path.dirname(path.abspath(context['file']))

        currpath = origpath
        while True:
            if path.basename(currpath) == arg:
                return currpath
            else:
                prevpath = currpath
                currpath = path.abspath(path.join(currpath, '..'))
                if currpath == prevpath:
                    raise Exception('Closest parent "' + arg + ' could not be found')

    raise Exception('Xacro command "' + op + ' not supported')
    