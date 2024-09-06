

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    counter = 0
    string_length = len(string)
    substring_length = len(substring)
    for i in range(string_length-substring_length):
        if string[i:substring_length+i] == substring:
            counter += 1
    return counter
