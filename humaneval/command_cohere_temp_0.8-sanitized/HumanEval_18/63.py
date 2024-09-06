def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): The original string.
        substring (str): The substring to search for.
    
    Returns:
        int: The number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    n, m = len(string), len(substring)
    count = 0
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    
    return count