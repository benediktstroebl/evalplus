```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    # Handle edge case where substring is empty
    if not substring:
        return 0
    
    # Initialize count to 0
    count = 0
    
    # Initialize the starting index for the search
    start = 0
    
    # Loop until we've searched the entire string
    while start < len(string):
        # Find the index of the substring in the string, starting at the current position
        index = string.find(substring, start)
        
        # If the substring was not found, exit the loop
        if index == -1:
            break
        
        # Increment the count
        count += 1
        
        # Move the start index to the position after the found substring
        start = index + 1
    
    # Return the total count
    return count

# Test the function
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```