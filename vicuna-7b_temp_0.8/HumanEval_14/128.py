from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string]
    for i, c in enumerate(string):
        prefixes = [prefix + c for prefix in prefixes]
        prefixes.remove(string)
    return prefixes
