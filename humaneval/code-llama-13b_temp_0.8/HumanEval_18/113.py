

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(substring) == 0:
        return 0
    elif len(string) < len(substring):
        return 0
    elif len(string) == len(substring):
        if string == substring:
            return 1
        else:
            return 0
    else:
        times = 0
        for i in range(len(string) - len(substring) + 1):
            if string[i:i + len(substring)] == substring:
                times += 1
        return times
