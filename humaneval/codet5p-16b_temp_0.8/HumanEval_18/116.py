

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
    sub_len = len(substring)
    string_len = len(string)
    for start in range(string_len - sub_len + 1):
        if string[start:start+sub_len] == substring:
            counter += 1
    return counter
