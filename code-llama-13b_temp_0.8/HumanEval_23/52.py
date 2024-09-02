

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


    'name': 'String Length',
    'params': [{'name': 'string', 'type': 'str'}],
    'description': 'Return length of given string',
    'pre_code': "strlen = lambda string: len(string)",
    'post_code': '',
    'weight': 1,
    'test': {
        'input': {'string': 'abc'},
        'output': 3
    },
    'analysis_process': [
        'Use the len method to find string length'
    ]
