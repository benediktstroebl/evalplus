from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes

