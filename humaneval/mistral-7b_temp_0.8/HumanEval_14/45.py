from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # this is a generalized solution,
    # you can also directly use a list comprehension like this:
    # return [s[:i] for i in range(len(s) + 1)]
    return list(range(len(string) + 1))

