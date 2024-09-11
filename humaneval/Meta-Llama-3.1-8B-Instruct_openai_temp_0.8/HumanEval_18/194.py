```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    i = 0
    
    # Loop through the string until we've checked all possible substrings
    while i < len(string):
        # Check if the substring is present at the current position
        if string[i:i+len(substring)] == substring:
            # If it is, increment the count and move the position forward by 1
            count += 1
            i += 1
        else:
            # If it's not, move the position forward by 1
            i += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```