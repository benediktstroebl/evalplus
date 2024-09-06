from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    # Create a dictionary where the key is the length of the string and the value is the string
    strings_dict = {}
    for string in strings:
        strings_dict[len(string)] = string

    # Get the max key
    if len(strings_dict) > 0:
        return strings_dict[max(strings_dict.keys())]
    else:
        return None

