

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    overlaping_count = 0
    string_length = len(string)
    substring_length = len(substring)
    for i in range(0, string_length - substring_length + 1):
        if string[i] == substring[0]:
            if string[i:i+substring_length] == substring:
                overlaping_count += 1
    return overlaping_count

