def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    
    Args:
        string (str): The original string.
        substring (str): The substring to search for.
    
    Returns:
        int: The number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    count = 0
    i = 0
    j = 0
    
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                count += 1
            i += 1
            j += 1
        elif j > 0:
            j -= 1
            if j == 0 and i < len(string):
                i += 1
                j += 1
        else:
            i += 1
            
    return count