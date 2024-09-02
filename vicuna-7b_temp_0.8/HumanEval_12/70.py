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
    # Sort the list in reverse order of length
    strings.sort(reverse=True)

    # Find the index of the last non-null string in the list
    last_index = len(strings) - 1
    last_index = strings.index(None, last_index)

    # If the last non-null string is the longest one, return its value
    if last_index == len(strings) - 1:
        return strings[last_index].strip()

    # If the last non-null string is not the longest one, return None
    return None

