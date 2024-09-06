from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_len = len(string)
    for prefix in string:
        prefix_len = len(prefix)
        if prefix_len < current_len:
            prefixes.append(prefix)
        else:
            prefixes.append(prefix[:current_len])
    return prefixes