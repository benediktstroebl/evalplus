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
    longest_string = None
    if strings:
        strings_length = list(map(lambda x: len(x), strings))
        longest_string = strings[strings_length.index(max(strings_length))]
    return longest_string

