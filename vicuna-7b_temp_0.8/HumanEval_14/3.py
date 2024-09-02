from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    suffixes = list(reversed(string))
    prefixes = [string[i:j] for i, j in zip(range(len(suffixes)), range(len(suffixes[0])-1, -1, -1))]
    prefixes.reverse()
    return prefixes

