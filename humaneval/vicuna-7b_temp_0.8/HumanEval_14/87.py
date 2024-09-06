from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chars = string.upper().split()
    prefixes = []
    for prefix in string_chars:
        prefix_len = len(prefix)
        prefixes.extend(prefixes[:prefix_len])
    prefixes.extend(prefixes)
    return prefixes
