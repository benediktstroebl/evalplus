def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    if substring == string:
        return 1
    
    counter = 0
    n, m = len(string), len(substring)
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            counter += 1
    
    return counter