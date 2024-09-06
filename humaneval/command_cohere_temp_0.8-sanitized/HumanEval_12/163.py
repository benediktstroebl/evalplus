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
    max_str: Optional[str] = None
    for str_ in strings:
        if len(str_) > len(max_str):
            max_str = str_
        elif len(str_) == len(max_str) and str_ > max_str:
            max_str = str_
    if not max_str and strings:
        max_str = strings[0]
    return max_str