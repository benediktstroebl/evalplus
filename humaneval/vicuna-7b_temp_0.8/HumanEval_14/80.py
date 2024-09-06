from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.lower()
    prefixes = []
    for i in range(len(string)):
        prefix = string[:i]
        prefixes.append(prefix)
        if i < len(string) - 1:
            prefixes.append(string[i:])
    return prefixes

