from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = string[0]
    for i in range(1, len(string)):
        prefixes.append(current_prefix + string[i:])
        current_prefix = string[i+1:].join()
    return prefixes

