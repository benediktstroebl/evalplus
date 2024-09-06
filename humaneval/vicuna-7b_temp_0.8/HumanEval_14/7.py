from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = string
    while current:
        prefixes.append(current)
        current = current[0]
    prefixes.reverse()
    return prefixes

