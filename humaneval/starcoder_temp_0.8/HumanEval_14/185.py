from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        return all_prefixes(string[:-1]) + [string[:-1]]

