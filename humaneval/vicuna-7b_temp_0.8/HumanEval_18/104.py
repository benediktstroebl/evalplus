

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
    start = 0
    end = 0
    
    for c in string:
        if c == substring[end]:
            count += 1
            start = end
            end += 1
        elif c == substring[end]:
            count += 1
            start = end
            end = 0
        else:
            start = end + 1
            
    count += 1
    return count