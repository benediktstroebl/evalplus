```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    # If the substring is empty, return 0
    if not substring:
        return 0
    
    # Initialize count to 0
    count = 0
    
    # Initialize the start index to 0
    start = 0
    
    # Loop until the substring is not found in the string
    while True:
        # Find the index of the substring in the string, starting from the start index
        index = string.find(substring, start)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count
        count += 1
        
        # Update the start index to the index after the found substring
        start = index + 1
    
    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. It uses the `find` method to search for the substring in the string, and updates the start index after each found substring to continue searching from the end of the previous match. The script also includes docstrings and test cases to demonstrate its usage and correctness.