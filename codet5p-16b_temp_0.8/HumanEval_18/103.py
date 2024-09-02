

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    start_index = 0
    count = 0
    while start_index!= -1:
        start_index = string.find(substring, start_index)
        if start_index!= -1:
            count += 1
            start_index += 1
    return count
