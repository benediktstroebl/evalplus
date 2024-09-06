from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = str(string)
    prefixes = []
    for prefix in string:
        prefix_length = len(prefix)
        for i in range(1, prefix_length + 1):
            prefixes.append(prefix[:i] + '0' * (prefix_length - i))
    return prefixes

