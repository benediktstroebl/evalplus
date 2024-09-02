from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.upper()
    prefixes = []
    for prefix in string:
        prefixes.append(prefix)
        prefixes.extend(string[:prefix].upper())
    return prefixes

