from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if not isinstance(string, str):
        raise TypeError('Input must be a string')
    result = ['']
    for ch in string:
        result = [pre + ch for pre in result]
    return result

