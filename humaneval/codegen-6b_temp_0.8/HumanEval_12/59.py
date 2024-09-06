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
    string_length: int = len(strings[0])
    longest: str = strings[0]
    for temp_string in strings:
        if len(temp_string) > string_length:
            string_length = len(temp_string)
            longest = temp_string
    return longest

