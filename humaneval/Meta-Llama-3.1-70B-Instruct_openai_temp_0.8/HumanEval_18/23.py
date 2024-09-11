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

    # Check if the substring is empty, in which case it's considered to be found 0 times
    if not substring:
        return 0

    # Initialize a counter to keep track of the number of times the substring is found
    count = 0

    # Iterate over the string, considering all substrings of the same length as the substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the current substring matches the substring we're looking for
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1

    # Return the total count of substrings found
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```