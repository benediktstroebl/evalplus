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
    if len(strings) == 0:
        return None

    longest_len = len(strings[0])
    longest_word = strings[0]

    for word in strings:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_word = word

    return longest_word

