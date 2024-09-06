

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    n = len(string)
    m = len(substring)
    num_of_times = 0
    i = 0
    while i < n - m + 1:
        if string[i:i+m] == substring:
            num_of_times += 1
            i += m
        else:
            i += 1
    return num_of_times

