from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.upper()  # case-insensitive
    prefixes = []
    current = []
    for i in range(len(string)):
        if i == 0:
            prefixes.append(current)
            current = [string[i:]]
        else:
            current.append(string[i:i+1])
    prefixes.append(current)
    return prefixes

