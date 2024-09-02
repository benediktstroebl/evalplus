

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter = 0
    last_index = 0
    index = string.find(substring, last_index)
    while index!= -1:
        last_index = index
        counter += 1
        index = string.find(substring, index + 1)
    return counter
