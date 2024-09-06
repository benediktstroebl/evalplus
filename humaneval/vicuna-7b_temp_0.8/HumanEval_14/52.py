from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_len = len(string)
    prefixes = [string[:i] for i in range(1, string_len + 1)]
    prefixes = [p for p in prefixes if p != string]
    return prefixes

