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
    # Empty list case
    if not strings:
        return None
    max_len = 0
    max_string = ""
    # Go through each string in the list
    for string in strings:
        # If the length of the string is greater than the max, then assign the string to max_string and update max_len
        if len(string) > max_len:
            max_string = string
            max_len = len(string)
        # Else if they are the same length, just update max_string to be the first string of that length
        elif len(string) == max_len:
            max_string = min(max_string, string)
    return max_string

