from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_list = string.split()
    prefixes = []
    for prefix in string_list:
        prefixes.append(prefix)
    prefixes.sort(reverse=True)
    return prefixes

