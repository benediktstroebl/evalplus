```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

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

    # Handle edge cases where the string or substring is empty
    if not string or not substring:
        return 0

    # Initialize count to 0
    count = 0

    # Iterate over the string with a sliding window of size equal to the substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the substring matches the current window
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the count
            count += 1

    # Return the total count
    return count
```