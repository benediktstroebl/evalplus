

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if len(substring) == 0 or len(string) == 0:
        return 0
    
    times = 0
    while True:
        if string.find(substring) == -1:
            return times

        times += 1
        string = string[string.find(substring) + 1:]

    return times

