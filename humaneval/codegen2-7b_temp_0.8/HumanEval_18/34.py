

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0
    pos = 0
    while True:
        pos = string.find(substring, pos)
        if pos == -1:
            break
        times += 1
        pos += 1
    return times
