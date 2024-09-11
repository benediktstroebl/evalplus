```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.

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
    
    # Loop through the string, with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i + len(substring)] == substring:
            # If it does, increment the count
            count += 1
    
    # Return the total count
    return count

# Test cases
if __name__ == "__main__":
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
```