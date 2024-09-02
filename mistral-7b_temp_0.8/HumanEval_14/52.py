from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # 1
    prefixes = []
    # 2
    for i in range(1, len(string)+1):
        # 3
        prefixes.append(string[:i])
    # 4
    return prefixes

