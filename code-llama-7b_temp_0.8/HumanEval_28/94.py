from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # version 1
    # return ''.join(strings)

    # version 2
    # result = ''
    # for string in strings:
    #     result += string
    # return result

    # version 3
    # result = ''
    # while strings:
    #     result += strings.pop()
    # return result

    # version 4
    # return reduce(lambda a, b: a + b, strings, '')

    # version 5
    # return reduce(lambda a, b: a + b, strings)

    # version 6
    # return ''.join(strings) if strings else ''

    # version 7
    # return ''.join(strings) if strings else ''

    # version 8
    # return '' if not strings else ''.join(strings)

    # version 9
    # return strings[0] if not strings[1:] else strings[0] + concatenate(strings[1:])

    # version 10
    # return strings[0] + concatenate(strings[1:]) if strings else ''

    # version 11
    # return '' if not strings else strings[0] + concatenate(strings[1:])

    # version 12
    # return strings[0] + concatenate(strings[1:]) if strings else ''

    # version 13
    # return reduce(lambda a, b: a + b, strings) if strings else ''

    # version 14
    # return reduce(lambda a, b: a + b, strings) if strings else ''

    # version 15
    # return '' if not strings else strings[0] + concatenate(strings[1:])

    # version 16
    # return '' if not strings else strings[0] + concatenate(strings[1:])

    # version 17
    # return '' if not strings else strings[0] + concatenate(strings[1:])

    # version 18
    # return '' if not strings else strings[0] + concatenate(strings[1:])

    # version 19
    # return strings[0]
