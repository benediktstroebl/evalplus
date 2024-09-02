from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # use slicing to return prefixes from the input string
    return string[0:].split("") + string[1:].split("") + string[2:].split("")