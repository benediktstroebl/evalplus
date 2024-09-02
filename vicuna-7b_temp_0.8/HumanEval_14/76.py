from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for prefix in string:
        prefixes.append(prefix)
        if prefix != string[0]:
            prefixes.sort(key=lambda x: len(x), reverse=True)
        prefixes.append(prefix)
    return prefixes

