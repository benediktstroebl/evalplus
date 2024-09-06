

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
    if m == 0:
        return n + 1
    if m > n:
        return 0
    i = j = count = 0
    while i < n and j < m:
        if string[i] == substring[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1
        if j == m:
            count += 1
            j = 0
    return count

