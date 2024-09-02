

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if substring in string:
        idx = 1
        while True:
            idx = string.find(substring, idx)
            if idx == -1:
                break
            count += 1
            idx += 1
    return count

from collections import defaultdict
