from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Find all possible prefixes
    prefixes = list(string)
    for i in range(1, len(string)+1):
        prefixes = [prefix + 'b' for prefix in prefixes]
        prefixes = [prefix for prefix in prefixes if prefix != 'ab']
    prefixes.reverse()
    # Return list of prefixes sorted by length
    return prefixes

