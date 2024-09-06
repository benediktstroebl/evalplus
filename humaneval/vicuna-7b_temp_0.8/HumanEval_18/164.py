

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    start_idx = 0
    end_idx = 0
    
    while start_idx <= len(string) and end_idx <= len(substring):
        if string[start_idx:end_idx] == substring:
            count += 1
            start_idx += len(substring)
        end_idx += len(substring)
        
    return count
