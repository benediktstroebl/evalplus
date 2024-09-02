

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    result = 0
    last_idx = 0
    for idx in range(len(string)):
        if string[idx:idx+len(substring)] == substring:
            result += 1
            last_idx = idx + len(substring)
    return result
