

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
    length = len(substring)
    for char in string:
        if substring[0] == char[0] and substring[1] == char[1]:
            count += 1
        elif length == 1:
            if substring == char:
                count += 1
        elif length == 2:
            if substring == char[:2] and char[2:] == substring[1:]:
                count += 1
        elif length == 3:
            if substring == char[:3] and char[3:] == substring[1:]:
                count += 1
    return count