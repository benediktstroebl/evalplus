```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Parameters:
    string (str): The original string to search in.
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
    # Initialize count to 0
    count = 0
    # If the substring is empty, return 0
    if not substring:
        return 0
    # Iterate over the string with a sliding window of length equal to the substring
    for i in range(len(string)):
        # Check if the substring matches the current window
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the count
            count += 1
    # Return the total count
    return count

# Test the function
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a simple iterative approach to count the occurrences of the substring in the string, allowing for overlapping matches. The time complexity of this solution is O(n*m), where n is the length of the string and m is the length of the substring.