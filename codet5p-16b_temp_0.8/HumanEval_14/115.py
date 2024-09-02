from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefixes = ['']
    for i in range(len(string)):
        new_prefixes = []
        for prefix in prefixes:
            new_prefixes.append(prefix)
            new_prefixes.append(prefix + string[i])
        prefixes = new_prefixes
    return prefixes

