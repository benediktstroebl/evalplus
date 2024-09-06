from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Convert string to list of characters, then to set
    string_set = set(string)
    prefixes = sorted(string_set, key=len)

    # Return prefixes as a list
    return prefixes

