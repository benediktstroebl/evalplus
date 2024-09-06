

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    overlaping_count = 0
    index_start = 0
    while index_start < len(string):
        index_end = string.find(substring, index_start)
        if index_end == -1:
            return overlaping_count
        index_start = index_end + 1
        overlaping_count += 1
    return overlaping_count
