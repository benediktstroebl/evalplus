from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # a list for storing all the prefixes
    res = []

    # enumerate till length of the string
    for i in range(len(string) + 1):
        # storing all prefixes
        res.append(string[:i])

    return res

