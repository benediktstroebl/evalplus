from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    current = string[0]
    for i in range(1, len(string)):
        for prefix in prefixes:
            if string[i:].startswith(prefix + current):
                prefixes.append(prefix + current)
                break
        else:
            prefixes.append(current)
        current = string[i]
    return prefixes

