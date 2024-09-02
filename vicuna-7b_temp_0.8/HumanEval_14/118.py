from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.upper()  # ensure uppercase string
    prefixes = []
    for prefix in string:
        prefixes.extend(string[:prefix])  # get all prefixes
    prefixes.reverse()  # reverse list to get longest prefix first
    return prefixes

