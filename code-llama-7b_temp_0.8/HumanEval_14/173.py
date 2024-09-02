from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # O(n * k) time | O(k) space
    # Where n is the length of the string, and k is the length of the prefix

    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i + 1])

    return prefixes

