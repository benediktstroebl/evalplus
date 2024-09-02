from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_length = len(string)
    for prefix in string:
        prefixes.append(prefix)
        if current_length == len(prefix):
            current_length -= len(prefix)
    return prefixes