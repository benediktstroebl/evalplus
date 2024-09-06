from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = string[0]
    for i in range(1, len(string)):
        if current_prefix == string[i]:
            prefixes.append(current_prefix)
        else:
            prefixes.append(current_prefix[1:])
            current_prefix = current_prefix[:-1]
    prefixes.append(current_prefix[1:])
    return prefixes

