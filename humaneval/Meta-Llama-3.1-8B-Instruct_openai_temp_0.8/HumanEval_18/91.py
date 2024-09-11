```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    # Initialize count to 0
    count = 0
    
    # If the substring is empty, return 0
    if substring == '':
        return 0
    
    # Loop over the string with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i + len(substring)] == substring:
            # If it matches, increment the count
            count += 1
    
    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```