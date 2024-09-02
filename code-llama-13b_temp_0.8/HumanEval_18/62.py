

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
    len_sub = len(substring)
    len_str = len(string)
    if len_sub == 0 or len_str == 0:
        return 0
    for i in range(len(string)):
        if string[i: i + len_sub] == substring:
            times += 1
    return times
