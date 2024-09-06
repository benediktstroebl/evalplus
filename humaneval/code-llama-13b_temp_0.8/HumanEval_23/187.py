

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


    'name': 'String Length',
    'params': [
        {
            'name': 'string',
            'type': 'string',
            'required': True
        }
    ],
    'return': {
        'type': 'int',
        'description': 'Length of the string'
    }
