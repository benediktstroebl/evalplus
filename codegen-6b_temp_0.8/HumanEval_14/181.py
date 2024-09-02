from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    all_prefixes = []
    for i in range(len(string)):
        prefix = string[:i+1]
        all_prefixes.append(prefix)
    return all_prefixes

