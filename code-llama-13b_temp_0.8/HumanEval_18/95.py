

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
    i = 0
    while i != len(string):
        j = 0
        while i + j != len(string) and j != len(substring) and string[i + j] == substring[j]:
            j += 1
        if j == len(substring):
            times += 1
            i += 1
        else:
            i += 1
    return times

