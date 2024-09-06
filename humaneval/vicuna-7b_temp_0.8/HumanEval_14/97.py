from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string_split = string.split('')
    prefixes = [string_split[0]]
    for prefix in string_split[1:]:
        prefixes.extend(prefixes[:-1] + [prefix])
    return prefixes

