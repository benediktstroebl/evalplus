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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Handle edge case where substring is empty or longer than string
    if not substring or len(substring) > len(string):
        return 0

    # Initialize count to 0
    count = 0

    # Iterate over the string, with the index going up to the point where the substring can still fit
    for i in range(len(string) - len(substring) + 1):
        # Check if the substring matches the string at the current index
        if string[i:i + len(substring)] == substring:
            # If it matches, increment the count
            count += 1

    # Return the count
    return count


# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```