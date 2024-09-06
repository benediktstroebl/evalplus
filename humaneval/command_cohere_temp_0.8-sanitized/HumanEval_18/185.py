def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): Original string.
        substring (str): Substring to search for.
    
    Returns:
        int: Number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    counter = 0
    length = len(substring)
    n = len(string)
    
    for i in range(n - length + 1):
        if string[i:i+length] == substring:
            counter += 1
    
    return counter