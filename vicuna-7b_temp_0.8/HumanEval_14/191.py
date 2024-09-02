from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = ''
    for char in string:
        if current_prefix + char == string:
            prefixes.append(current_prefix)
            current_prefix = ''
        else:
            current_prefix += char
    prefixes.append(current_prefix)
    return prefixes

