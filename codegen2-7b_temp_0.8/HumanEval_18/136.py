

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    i = 0
    while True:
        i += 1
        if i > len(string):
            return 0
        if string[i-1] == substring[0]:
            s = 0
            for j in range(i):
                if string[j] == substring[s]:
                    s += 1
                    if s == len(substring):
                        return i - j
        else:
            i = 0
