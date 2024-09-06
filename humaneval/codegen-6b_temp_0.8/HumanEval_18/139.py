

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    index_left = 0
    while string.find(substring, index_left) != -1:
        index_left = string.find(substring, index_left) + 1
    return index_left - 1

