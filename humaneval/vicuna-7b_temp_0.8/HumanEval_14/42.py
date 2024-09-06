from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string) + 1):
        prefix = string[:i]
        prefixes.append(prefix)
        if string[i:].startswith(prefix):
            prefixes.append(prefix + string[i:])
    return prefixes

