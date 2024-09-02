

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    start = 0
    times = 0

    while True:
        start = string.find(substring, start, len(string))
        if start == -1:
            return times
        else:
            times += 1
            start += 1
