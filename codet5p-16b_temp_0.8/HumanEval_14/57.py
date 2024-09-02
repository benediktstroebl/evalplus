from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    all_prefixes = []
    for i in range(len(string)):
        all_prefixes.append(string[:i+1])
    return all_prefixes

