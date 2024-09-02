from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = str(string)
    prefixes = [string]
    for i in range(len(string) - 1, 0, -1):
        for j in range(len(string) - i):
            prefixes.append(string[j:i] + string[i])
    return prefixes

