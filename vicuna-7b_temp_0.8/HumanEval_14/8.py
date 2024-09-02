from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chars = string.upper().split()
    prefixes = [string_chars[i:j] for i in range(len(string_chars)) for j in range(i+1, len(string_chars))]
    return sorted(prefixes, key=lambda x: len(x))

