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
    """
    # Handle edge case where substring is empty
    if not substring:
        return 0

    count = 0
    start = 0

    # Loop through the string to find the substring
    while start < len(string):
        # Find the substring in the string, starting from the current position
        pos = string.find(substring, start)

        # If the substring is not found, exit the loop
        if pos == -1:
            break

        # Increment the count and move the start position to the character after the found substring
        count += 1
        start = pos + 1

    return count


# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

Alternatively, you can use a more Pythonic approach using `str.count` and a loop to account for overlapping substrings:

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
    """
    count = 0
    start = 0

    # Loop through the string to find the substring
    while start < len(string):
        # Find the substring in the string, starting from the current position
        pos = string.find(substring, start)

        # If the substring is not found, exit the loop
        if pos == -1:
            break

        # Increment the count and move the start position to the character after the found substring
        count += 1
        start = pos + 1

    return count
```