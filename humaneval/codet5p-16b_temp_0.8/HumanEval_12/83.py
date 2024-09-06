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
    elif len(strings) == 1:
        return strings[0]
    else:
        lengths = [len(s) for s in strings]
        max_length = max(lengths)
        indices_of_max_lengths = [i for i, j in enumerate(lengths) if j == max_length]
        return max(strings, key=lambda s: len(s)) if len(indices_of_max_lengths) > 1 else strings[indices_of_max_lengths[0]]
    
