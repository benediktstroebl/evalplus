

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
    start = 0
    sublength = len(substring)
    length = len(string)
    while start < length:
        pos = string.find(substring, start)
        if pos == -1:
            break
        start = pos + sublength
        times += 1
    return times

