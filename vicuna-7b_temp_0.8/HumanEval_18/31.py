

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
    start = 0
    end = 0
    for char in string:
        if char == substring[end]:
            end = end + 1
        elif end == 0:
            start = char
            end = end + 1
    count = max(count, end - start)
    return count