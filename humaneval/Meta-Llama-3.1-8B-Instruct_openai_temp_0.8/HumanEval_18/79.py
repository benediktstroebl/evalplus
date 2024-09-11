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
    """
    
    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize count to 0
    count = 0

    # Loop through the string, sliding the window of substring length
    for i in range(len(string) - len(substring) + 1):
        # Check if the substring matches at the current position
        if string[i:i + len(substring)] == substring:
            # If it matches, increment the count
            count += 1

    # Return the total count
    return count


# Test cases
print(how_many_times('', 'a'))     # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script achieves the desired functionality by iterating over the input string and checking for the presence of the substring at each position. It uses a sliding window approach to count overlapping matches. The test cases at the end verify that the function behaves as expected.