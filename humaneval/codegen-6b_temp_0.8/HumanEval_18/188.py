

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # if len(string) < len(substring):
    #     return 0
    # if len(string) == len(substring):
    #     return 1 if string == substring else 0
    # else:
    #     return sum([1 for i in range(len(string)) if string[i:i+len(substring)] == substring])

    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        return 1 if string == substring else 0
    else:
        return 1 + sum([string[i:i+len(substring)] == substring for i in range(len(string))])


