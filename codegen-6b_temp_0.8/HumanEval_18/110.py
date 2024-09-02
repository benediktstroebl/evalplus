

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string:
        return 0
    elif not substring:
        return 0
    elif len(substring) > len(string):
        return 0
    total_count = 0
    for i in range(len(string) - len(substring) + 1):
        tc = 0
        for j in range(len(substring)):
            if substring[j] == string[i+j]:
                tc += 1
        if tc == len(substring):
            total_count += 1
    return total_count

