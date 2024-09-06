from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_len = len(string)
    for char in string:
        prefixes.append(char)
        if current_len == len(string):
            prefixes.pop()
            current_len = len(string)
    prefixes.append(char)
    return prefixes