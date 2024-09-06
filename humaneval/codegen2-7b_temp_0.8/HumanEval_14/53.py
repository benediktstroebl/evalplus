from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    n = len(string)
    if n == 0:
        return []
    return [string[0]] + all_prefixes(string[1:]) if n > 1 else
