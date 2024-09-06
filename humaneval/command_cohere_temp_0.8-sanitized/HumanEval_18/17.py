def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): Original string.
        substring (str): Substring to search for.
    
    Returns:
        int: Number of times substring occurs in the original string.
    """
    if not string or not substring:
        return 0
    
    count = 0
    n = len(string)
    m = len(substring)
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    
    return count