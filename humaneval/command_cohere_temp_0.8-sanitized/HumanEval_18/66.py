def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlaping cases."""
    if not string or not substring:
        return 0
    
    num_occurrences = 0
    
    # Using a loop to find occurrences for efficiency and to handle overlapping cases
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            num_occurrences += 1
    
    return num_occurrences