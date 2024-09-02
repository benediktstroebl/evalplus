from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


    'name': 'Concatenate',
    'author': 'Seth M. Morton',
    'url': 'http://www.sethmorton.com/',
    'description': 'Concatenates a list of strings into a single string.',
    'sample': 'concatenate([]) == "" and concatenate(["a", "b", "c"]) == "abc"'

