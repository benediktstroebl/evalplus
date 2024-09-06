

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
    for i in range(string_length):
        if substring in string[i:i+substring_length]:
            count += 1
    return count