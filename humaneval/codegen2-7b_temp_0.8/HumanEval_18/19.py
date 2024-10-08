

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
    while string and substring:
        if string[0] == substring[0]:
            count += 1
            string = string[1:]
            substring = substring[1:]
        else:
            string = string[1:]
    return
