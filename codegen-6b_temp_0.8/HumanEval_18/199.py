

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    occurences = 0
    next_index = 0
    while True:
        index = string.find(substring, next_index)
        if index == -1:
            break
        occurences += 1
        next_index = index + 1
    return occurences
