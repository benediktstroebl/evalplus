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

    def longest_string(s1: str, s2: str) -> str:
        if len(s1) > len(s2):
            return s1
        elif len(s1) < len(s2):
            return s2
        else:
            return s1

    longest_string_so_far = strings[0]

    for s in strings[1:]:
        longest_string_so_far = longest_string(s, longest_string_so_far)

    return longest_string_so_far

