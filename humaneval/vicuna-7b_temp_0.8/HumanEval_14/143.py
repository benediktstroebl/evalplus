from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.lower()
    prefixes = []
    for prefix in string:
        if len(prefix) == len(string):
            prefixes.append(prefix)
    return prefixes

