

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times: int = 0
    i: int = 0
    while i < len(string):
        index: int = string.find(substring, i)
        if index!= -1:
            times += 1
            i = index + 1
        else:
            break
    return times
