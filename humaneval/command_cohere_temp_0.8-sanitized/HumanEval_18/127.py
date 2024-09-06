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
    string = string.replace(substring, '**' + substring + '**')
    count = string.count('**' + substring + '')
    return count // 2