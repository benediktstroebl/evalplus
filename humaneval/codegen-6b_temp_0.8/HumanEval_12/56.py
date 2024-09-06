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
    strings = list(strings)
    if not strings:
        return None
    # get the length of the first item
    item_len = len(strings[0])
    max_len = len(strings[0])
    max_string = strings[0]
    # index of the max_string index
    max_string_idx = 0
    # loop over index
    for i in range(len(strings)):
        item = strings[i]
        if len(item) > max_len:
            max_len = len(item)
            max_string = item
            max_string_idx = i

    return strings[max_string_idx]

