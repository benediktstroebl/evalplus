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
    if not strings:
        return None
    if len(strings) == 1:
        return strings[0]
    strings_sorted = sorted(strings, key=len, reverse=True)
    longest_string = strings_sorted[0]
    string_length = len(longest_string)
    for string in strings_sorted:
        if len(string) < string_length:
            break
        longest_string = string
    return longest_string



