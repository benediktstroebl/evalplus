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
    else:
        max_len = max([len(s) for s in strings])
        max_len_strings = list(filter(lambda s: len(s) == max_len, strings))
        return min(max_len_strings, key=lambda x: strings.index(x))

