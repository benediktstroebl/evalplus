

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    string_len = len(string)
    substring_len = len(substring)
    times = 0
    for i in range(string_len - substring_len + 1):
        if string[i : i + substring_len] == substring:
            times += 1
    return times

