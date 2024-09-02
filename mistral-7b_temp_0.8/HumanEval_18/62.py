

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
    if string_len < substring_len:
        return 0
    if string_len == substring_len and string == substring:
        return 1
    if string_len == substring_len and string != substring:
        return 0
    index = 0
    count = 0
    while index < string_len:
        if string[index:index+substring_len] == substring:
            count += 1
        index += 1
    return count

