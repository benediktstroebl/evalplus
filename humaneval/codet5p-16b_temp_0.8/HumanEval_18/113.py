

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    how_many = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i : i + sub_len] == substring:
            how_many += 1
    return how_many
