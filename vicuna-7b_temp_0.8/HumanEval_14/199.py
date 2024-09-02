from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_len = len(string)
    for prefix in string:
        prefixes.append(prefix)
        if current_len > len(prefix):
            current_len = len(prefix)
    prefixes.append(prefixes[0])
    return prefixes

