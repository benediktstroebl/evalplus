from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.lower()
    prefixes = []
    for prefix in string:
        prefixes.append(prefix)
        suffixes = [prefix+c for c in string[1:]]
        prefixes.extend(suffixes)
    prefixes.sort()
    return prefixes

