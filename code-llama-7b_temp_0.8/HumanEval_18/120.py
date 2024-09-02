

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if len(substring) > len(string):
        return 0
    if len(substring) == 0:
        return len(string)
    times = 0
    if substring in string:
        times += 1
        string = string.replace(substring, '', 1)
        times += how_many_times(string, substring)
    return times

