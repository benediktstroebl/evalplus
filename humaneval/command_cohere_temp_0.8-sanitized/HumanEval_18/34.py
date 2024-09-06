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
    
    num_times = 0
    num_times_previous = 0
    
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            if i != len(string) - len(substring) and string[i+len(substring)] != substring[0]:
                num_times_previous += 1
            else:
                num_times += 1
        elif num_times_previous > 0:
            num_times_previous -= 1
    
    return num_times