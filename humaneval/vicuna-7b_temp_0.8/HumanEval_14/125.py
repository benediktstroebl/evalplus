from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = string[0]
    for c in string:
        if current == c:
            prefixes.append(current)
            current = ""
        else:
            current += c
    prefixes.append(current)
    return prefixes

