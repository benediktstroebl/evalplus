from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if len(string) == 1:
        return [string]
    return all_prefixes(string[1:]) + [string[0] + i for i in all_prefixes(string[1:])]

