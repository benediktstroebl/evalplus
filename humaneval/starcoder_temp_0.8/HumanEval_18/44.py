

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count: int = 0
    length: int = len(string)
    substring_length: int = len(substring)
    for i in range(length-substring_length+1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count
