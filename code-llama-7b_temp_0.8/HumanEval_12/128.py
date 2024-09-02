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

    longest_string: str = max(strings, key=len)
    max_len: int = len(longest_string)
    same_length_strings: List[str] = [string for string in strings if len(string) == max_len]

    return longest_string if len(same_length_strings) == 1 else same_length_strings[0]

