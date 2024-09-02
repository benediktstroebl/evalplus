

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if substring not in string:
        return 0
    if len(substring) == 1:
        return string.count(substring)
    times = 0
    start_pos = 0
    while True:
        start_pos = string.find(substring, start_pos)
        if start_pos != -1:
            times += 1
            start_pos += 1
        else:
            return times

