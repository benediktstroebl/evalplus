def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    
    Args:
        string (str): The original string.
        substring (str): The substring to search for.
    
    Returns:
        int: Number of times substring appears in the original string.
    """
    if not string or not substring:
        return 0
    
    counter = 0
    length = len(substring)
    num_occurrences = 0
    
    for i in range(len(string) - length + 1):
        if string[i:i+length] == substring:
            counter += 1
            num_occurrences += counter
            
            # To count overlapping cases, we increment the counter again if we have a consecutive match.
            if i + length < len(string) and string[i+length] == substring[0]:
                counter += 1
    
    return num_occurrences