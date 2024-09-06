from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    n = len(string)
    return [string[:i + 1] for i in range(n)] + [string[:i + 1] for i in range(n, 0, -1)]
