

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    assert isinstance(string, str), f'The parameter `string` must be a string, not a {type(string)}.'
    assert isinstance(substring, str), f'The parameter `substring` must be a string, not a {type(substring)}.'
    
    assert 0 <= len(substring), f'The length of the `substring` must be non-negative, not {len(substring)}.'
    
    count = 0
    
    # Loop through the string and find all the indexes where the substring appears.
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    
    return count
