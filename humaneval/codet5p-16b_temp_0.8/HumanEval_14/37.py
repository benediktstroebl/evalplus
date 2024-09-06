from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if string is None:
        return []
    prefix = ''
    result = [prefix]
    for c in string:
        prefix += c
        result.append(prefix)
    return result

