

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    overlapping = 0
    start_pos = 0
    while True:
        start_pos = string.find(substring, start_pos)
        if start_pos == -1:
            return overlapping
        overlapping += 1
        start_pos += 1

