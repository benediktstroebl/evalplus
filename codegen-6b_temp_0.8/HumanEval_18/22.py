

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
    occurrences = 0
    n = len(string)
    m = len(substring)
    while i < n - m:
        if string[i] == substring[0]:
            if string[i:i + m] == substring:
                occurrences += 1
                i += m
            else:
                i += 1
        else:
            i += 1
    return occurrences
