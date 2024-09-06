

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if not string or not substring:
        return 0

    count = 0
    len_string = len(string)
    len_substring = len(substring)
    i = 0
    while i < len_string:
        if string[i:i+len_substring] == substring:
            count += 1
            i += len_substring
        else:
            i += 1
    return count
