from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for prefix in string:
        prefixes.extend(prefix for prefix in string if prefix.startswith(string))
    return prefixes

