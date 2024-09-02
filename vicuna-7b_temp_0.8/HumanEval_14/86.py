from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = string
    for prefix in current:
        prefixes.append(prefix)
        current = current[:-len(prefix)]
    return prefixes

