```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """

    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize a counter to keep track of the number of occurrences
    count = 0

    # Iterate over the string, considering substrings of the same length as the target substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the current substring matches the target substring
        if string[i:i + len(substring)] == substring:
            # If it does, increment the counter
            count += 1

    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

Alternatively, you can use a more concise solution using Python's built-in `str.count()` method, which also counts overlapping occurrences:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    return string.count(substring)

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```