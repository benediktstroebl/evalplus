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
    # This solution uses a dictionary where keys are length of the string and values are the strings
    # of that length. Then it returns the string with the longest length.
    # If there are multiple strings with the same length, it returns the first one.
    string_dict = {}
    for string in strings:
        string_dict.setdefault(len(string), []).append(string)

    longest_string = max(string_dict.keys()) if string_dict else None
    if longest_string:
        return string_dict[longest_string][0]
