from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return sorted(string[:i] for i in range(len(string) + 1) if string[i] == 'a' or string[i] == 'b' or string[i] == 'c')
