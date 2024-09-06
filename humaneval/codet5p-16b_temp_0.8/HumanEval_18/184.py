

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
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count
