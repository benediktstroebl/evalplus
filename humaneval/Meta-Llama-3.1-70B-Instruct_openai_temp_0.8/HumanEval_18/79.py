```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring is found in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:  # If substring is empty, return 0
        return 0
    
    count = 0  # Initialize count
    start = 0  # Initialize start pointer
    
    while start < len(string):  # Loop until start pointer reaches the end of the string
        pos = string.find(substring, start)  # Find the position of the substring
        
        if pos!= -1:  # If the substring is found
            count += 1  # Increment count
            start = pos + 1  # Move the start pointer to the next character
        else:
            break  # If the substring is not found, break the loop
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```