from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # base case
    if string == "":
        return []
    # recursive case
    # add the current string to the list
    prefixes = [string]
    # recursively call the function, except with an input of the current string
    # minus the first character, because we don't want to include the first character
    # in the substrings of our list
    prefixes.extend(all_prefixes(string[1:]))
    return prefixes

