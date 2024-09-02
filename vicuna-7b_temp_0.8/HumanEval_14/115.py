from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = string[0]
    for char in string[1:]:
        if current_prefix == char:
            prefixes.append(current_prefix)
            current_prefix = char
        else:
            prefixes.append(current_prefix)
            current_prefix = char
    prefixes.append(current_prefix)
    return prefixes