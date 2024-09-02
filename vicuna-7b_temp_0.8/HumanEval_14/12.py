from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = ''
    for c in string:
        if c == 'a':
            prefixes.append(current_prefix)
            current_prefix = 'b'
        elif c == 'b':
            prefixes.append(current_prefix)
            current_prefix = 'c'
        elif c == 'c':
            prefixes.append(current_prefix)
            current_prefix = ''
    prefixes.append(current_prefix)
    return prefixes