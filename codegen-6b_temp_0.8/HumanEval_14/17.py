from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    all_prefixes = [None] * (len(string) + 1)
    all_prefixes[0] = ''
    for i in range(1, len(string) + 1):
        all_prefixes[i] = string[:i]
    return all_prefixes

