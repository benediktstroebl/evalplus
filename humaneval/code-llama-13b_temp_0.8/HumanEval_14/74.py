from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    i = 1
    while i < len(string):
        result.append(string[:i])
        i += 1
    result.append(string)
    return result

