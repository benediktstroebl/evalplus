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
    lengths = {len(string) for string in strings}
    lengths.discard(0)
    if len(lengths) == 0:
        return None
    elif len(lengths) == 1:
        return strings[0]
    else:
        return strings[0] if len(strings[0]) == max(lengths) else None
    
    
