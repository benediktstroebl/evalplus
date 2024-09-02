from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    current = []
    for char in string:
        if len(current) > 0:
            result.append(current)
        current.append(char)
    result.reverse()
    return result

