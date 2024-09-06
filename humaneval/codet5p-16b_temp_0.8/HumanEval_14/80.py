from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefixes: List[str] = []

    if string == '':
        return prefixes

    prefixes.append(string[0:1])
    all_prefixes(string[1:])

    return prefixes
