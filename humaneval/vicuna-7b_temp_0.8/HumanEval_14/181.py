from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_chars = string
    prefixes = []
    while string_chars:
        prefixes.append(string_chars[0])
        string_chars = string_chars[1:]
    return prefixes
