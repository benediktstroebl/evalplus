from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # calculate length of input string
    l = len(string)

    # base case
    if l == 0:
        return []

    # helper function
    def prefixes(string, l):
        # add first letter to list
        prefix = [string[0]]

        # if more letters left, add all prefixes of remaining string
        if l > 1:
            prefix += [string[:i] for i in range(1, l)]
        return prefix

    # loop through all prefixes and add them to list
    return prefixes(string, l) + all_prefixes(string[1:])
