

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
    string_length = len(string)
    for i in range(0, string_length):
        if string[i:i+len(substring)] == substring:
            count = count + 1
    return count
