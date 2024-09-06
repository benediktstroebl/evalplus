

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    how_many = 0
    current_position = 0
    while True:
        next_position = string.find(substring, current_position)
        if next_position != -1:
            how_many += 1
            current_position = next_position + 1
        else:
            break
    return how_many

