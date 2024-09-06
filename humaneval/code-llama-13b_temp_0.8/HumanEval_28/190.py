from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # start with an empty string
    result = ''
    for string in strings:
        # add each string to the result
        result += string
    return result


    'name': 'Concatenation',
    'author': 'Anonymous',
    'description': 'Concatenate a list of strings into a single string',
    'url': 'https://stepik.org/lesson/14143/step/7',
    'source_url': 'https://en.wikipedia.org/wiki/Concatenation',
    'tags': ['strings', 'lists']
