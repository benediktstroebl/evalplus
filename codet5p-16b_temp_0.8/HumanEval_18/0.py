

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
    idx_substring = 0
    len_substring = len(substring)
    len_string = len(string)
    while idx_substring < len_substring and idx_substring < len_string:
        if string[idx_substring] == substring[idx_substring]:
            idx_substring += 1
            counter += 1
        else:
            idx_substring = 0
    return counter

