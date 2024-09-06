

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    string_length = len(string)
    substring_length = len(substring)
    count = 0
    start = 0
    while start < string_length:
        end = string.find(substring, start)
        if end == -1:
            break
        count += 1
        start = end + substring_length
    return count