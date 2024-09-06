

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
        if substring[0] == char and length > 0:
            count += 1
        elif length > 0:
            if substring[0] == char:
                count += 1
            for i in range(1, length):
                if string[i] == substring[i]:
                    count += 1
    return count
