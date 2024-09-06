from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current_prefix = []

    for x in string:
        if x == '':
            if len(current_prefix) > 0:
                prefixes.append(current_prefix)
                current_prefix = []
            continue
        current_prefix.append(x)

    prefixes.append(current_prefix)

    return prefixes

