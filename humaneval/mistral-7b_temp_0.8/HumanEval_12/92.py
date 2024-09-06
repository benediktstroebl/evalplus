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
    else:
        longest_strings = []
        for string in strings:
            if len(string) > len(longest_strings[-1]):
                longest_strings = [string]
            elif len(string) == len(longest_strings[-1]):
                longest_strings.append(string)
        return longest_strings[0]
