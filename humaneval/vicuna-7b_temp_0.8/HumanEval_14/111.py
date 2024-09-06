from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []

    prefixes = []
    current_prefix = string
    for i in range(len(current_prefix)):
        if current_prefix[i] != current_prefix[i+1]:
            prefixes.append(current_prefix[i:])
            current_prefix = current_prefix[:i]
        else:
            current_prefix = current_prefix[:i+1]
    prefixes.append(current_prefix)
    return prefixes

