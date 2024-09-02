

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
    if not string or not substring:
        return times
    len_substring = len(substring)
    for i in range(len(string)):
        if string[i:i+len_substring] == substring:
            times += 1
    return times

