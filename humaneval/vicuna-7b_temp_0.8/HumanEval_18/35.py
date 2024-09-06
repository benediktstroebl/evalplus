

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    string_len = len(string)
    substring_len = len(substring)
    count = 0
    i = 0
    while i < string_len:
        if string[i:i+substring_len] == substring:
            count += 1
            i += substring_len
    return count