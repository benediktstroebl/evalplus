from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    n = len(string)
    pfx = []
    for i in range(n):
        pfx.append(string[:i + 1])
    return pfx
