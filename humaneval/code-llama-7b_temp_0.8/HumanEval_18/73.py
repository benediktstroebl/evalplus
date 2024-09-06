

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    sub_len = len(substring)
    if sub_len == 0:
        return 0
    if sub_len > len(string):
        return 0
    counter = 0
    for i in range(len(string) - sub_len + 1):
        substr = string[i:i + sub_len]
        if substr == substring:
            counter += 1
    return counter

