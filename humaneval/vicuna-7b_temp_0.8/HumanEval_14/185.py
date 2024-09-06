from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[i:i+1] for i in range(len(string)-1)]
    return [prefix for prefix in prefixes if len(prefix) == 1]

