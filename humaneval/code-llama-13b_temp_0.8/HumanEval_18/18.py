

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    substring_length = len(substring)
    substring_position = 0
    count = 0
    while substring_position != -1:
        substring_position = string.find(substring, substring_position)
        if substring_position != -1:
            substring_position += substring_length
            count += 1

    return count

