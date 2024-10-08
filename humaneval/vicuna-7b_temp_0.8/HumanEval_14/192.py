from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = string[0]
    for i in range(1, len(string)):
        if string[i] == current:
            prefixes.append(current)
            current = string[i]
        else:
            prefixes.append(current)
            current = current + string[i]
    prefixes.append(current)
    return prefixes

