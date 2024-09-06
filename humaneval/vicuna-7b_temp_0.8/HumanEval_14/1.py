from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_len = len(string)
    for i in range(current_len, 0, -1):
        prefixes.append(string[i:])
    return prefixes

