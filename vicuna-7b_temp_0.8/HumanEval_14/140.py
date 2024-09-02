from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_len = len(string)
    prefixes = []
    for i in range(string_len):
        prefixes.append(string[i:])
    prefixes.reverse()
    return prefixes

