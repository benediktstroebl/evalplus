from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    if len(string) == 1:
        return [string]
    elif len(string) == 2:
        return [string[0], string[0] + string[1]]
    else:
        return [string[0], string[0] + string[1], string]

