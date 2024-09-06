from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.upper()
    prefixes = []
    current_prefix = []
    for i in range(len(string)):
        if string[i] in current_prefix:
            current_prefix.append(string[i])
            prefixes.append(current_prefix)
            current_prefix = []
        else:
            current_prefix.append(string[i])
    prefixes.append(current_prefix)
    return prefixes

