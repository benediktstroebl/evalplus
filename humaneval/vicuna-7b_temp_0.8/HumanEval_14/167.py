from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_len = len(string)
    prefixes = [string[i:i+1] for i in range(0, string_len, 1)]
    prefixes.reverse()
    return prefixes

