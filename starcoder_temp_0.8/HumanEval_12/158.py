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

    current_len = 0
    current_word = None

    for word in strings:
        if len(word) > current_len:
            current_word = word
            current_len = len(word)

    return current_word
