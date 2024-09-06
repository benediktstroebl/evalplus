from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_length = len(string)
    for i in range(1, current_length + 1):
        prefixes.append(string[i:i+1])
    return prefixes
