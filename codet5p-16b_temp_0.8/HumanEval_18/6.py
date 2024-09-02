

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
    length = len(string)
    sublength = len(substring)
    i = 0
    while i < length:
        if string[i:i+sublength] == substring:
            counter += 1
            i += sublength
        else:
            i += 1
    return counter

