

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0
    elif not string:
        return 0
    count = 0
    while True:
        position = string.find(substring)
        if position != -1:
            string = string[position + 1:]
            count += 1
        else:
            return count
