

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    start_at = 0
    counts = 0
    while True:
        find_index = string.find(substring, start_at)
        if find_index == -1:
            return counts
        counts += 1
        start_at = find_index + 1
