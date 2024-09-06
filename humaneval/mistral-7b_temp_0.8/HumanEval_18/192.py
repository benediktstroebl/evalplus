

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

    start_position = 0

    while True:
        start_position = string.find(substring, start_position)

        if start_position == -1:
            return count
        else:
            count += 1
            start_position += 1

