

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    
    substring_len = len(substring)
    substring_list = []

    for i in range(len(string)):
        if i+substring_len <= len(string) and string[i:i+substring_len] == substring:
            substring_list.append(substring)

    return len(substring_list)
