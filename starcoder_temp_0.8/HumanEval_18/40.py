

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    counter: int = 0
    string_length: int = len(string)
    substring_length: int = len(substring)
    for i in range(string_length):
        if string[i:substring_length + i] == substring:
            counter += 1
    return counter

