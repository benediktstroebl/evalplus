```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring is found in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Handle the edge case where the substring is empty
    if not substring:
        return 0

    # Initialize a counter variable
    count = 0

    # Iterate over the string with a sliding window of the substring's length
    for i in range(len(string) - len(substring) + 1):
        # Check if the substring matches the current window
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1

    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```