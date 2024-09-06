from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if len(string) == 0:
        return ['']
    else:
        first = string[0]
        rest = string[1:]
        return [first + prefix for prefix in all_prefixes(rest)] + [string]

