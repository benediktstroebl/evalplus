

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
    count = 0

    for i in range(n - m + 1):
        for j in range(m):
            if string[i + j] != substring[j]:
                break
        else:
            count += 1
    return count

