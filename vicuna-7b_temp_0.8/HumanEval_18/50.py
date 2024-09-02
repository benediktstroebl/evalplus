

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
    start_index = 0
    end_index = 0
    
    for i in range(len(string)):
        if string[i:i+1] == substring:
            count += 1
            start_index = i
            end_index = i
        elif string[i:i+1] == substring and start_index < end_index:
            end_index = i
            count += 1
        elif start_index < end_index:
            count += 1
            
    return count