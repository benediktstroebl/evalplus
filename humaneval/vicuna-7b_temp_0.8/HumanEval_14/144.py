from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    curr = ''
    for char in string:
        curr += char
        prefixes.append(curr)
        curr = ''
    prefixes.append(curr)
    return prefixes

