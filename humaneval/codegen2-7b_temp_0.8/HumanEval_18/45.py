

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    last_index = 0
    while True:
        if len(string) == 0:
            break
        index = string.find(substring, last_index)
        if index == -1:
            break
        last_index = index + 1
        count += 1
    return count
