

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    num = 0
    i = 0
    for char in string:
        if char == substring[i]:
            i += 1
        else:
            i = 0
        if i == len(substring):
            i = 0
            num += 1
    return num
