from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[0]]
    for prefix in string[1:]:
        prefixes.append(prefix)
        prefixes.extend(string[1:].split(prefix))
    return prefixes

