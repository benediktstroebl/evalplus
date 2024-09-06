

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


    'name': 'strlen',
    'tested': {
        'simple_test': {
            'name': strlen.__name__,
            'cases': [
                {'args': ['abc'], 'expected': 3},
                {'args': [''], 'expected': 0}
            ]
        }
    }
