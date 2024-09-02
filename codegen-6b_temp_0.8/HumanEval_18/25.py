

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
    if n < m:
        return 0
    elif string == '':
        return 0
    elif substring == '':
        return 1
    elif substring == string:
        return 1
    else:
        start = 0
        end = m
        while start < n and end < n + m:
            if string[start:end] == substring:
                start += m
            end += 1
        return end-start-m
