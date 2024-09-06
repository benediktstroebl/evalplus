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
    
    n, m = len(string), len(substring)
    
    # Ensure substring is shorter than the string
    if m > n:
        return 0
    
    counter = 0
    
    # Slide substring through string
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            counter += 1
    
    return counter