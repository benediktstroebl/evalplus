from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = ''
    for prefix in string:
        if prefix == current_prefix:
            prefixes.append(current_prefix)
        else:
            current_prefix = prefix
            prefixes.append(current_prefix)
    prefixes.append(current_prefix)
    return prefixes
