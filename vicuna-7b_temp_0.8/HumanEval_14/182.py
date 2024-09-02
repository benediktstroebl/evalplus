from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_list = list(string)
    prefixes = []

    for prefix in string_list:
        prefix_length = len(prefix)
        for i in range(prefix_length, len(string)):
            prefixes.append(string[i:])

    return prefixes

