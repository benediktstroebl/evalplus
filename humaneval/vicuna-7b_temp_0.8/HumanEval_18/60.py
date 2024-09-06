

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
    for i in range(len(string) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
            last_index = i + len(substring)
    return count
