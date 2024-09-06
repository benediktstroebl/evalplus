

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
    str_len = len(string)
    substr_len = len(substring)
    for i in range(str_len - substr_len + 1):
        if string[i:i+substr_len] == substring:
            result += 1
    return result

