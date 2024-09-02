

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
    len_substring = len(substring)
    for idx in range(len(string)):
        if string[idx:idx + len_substring] == substring:
            overlaping_count += 1
    return overlaping_count

