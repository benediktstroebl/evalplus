from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chars = string.lower().split()
    prefixes = [string_chars[i:] for i in range(len(string_chars) - 1)]
    prefixes.reverse()
    return prefixes

