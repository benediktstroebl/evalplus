

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # trivial case - substring not found
    if len(substring) > len(string):
        return 0

    num_times = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            num_times += 1

    return num_times


