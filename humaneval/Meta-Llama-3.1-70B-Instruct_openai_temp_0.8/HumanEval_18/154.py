```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be found.

    Returns:
    int: The number of times the substring can be found.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Handle edge case where string is empty
    if not string:
        return 0

    # Initialize count of occurrences
    count = 0

    # Iterate over the string with a sliding window of size equal to the substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the current window matches the substring
        if string[i:i+len(substring)] == substring:
            # If it does, increment the count
            count += 1

    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```
Alternatively, you can use the following more Pythonic solution using the `str.find` method:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be found.

    Returns:
    int: The number of times the substring can be found.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Initialize count of occurrences
    count = 0
    index = 0

    # Iterate over the string until we reach the end
    while index < len(string):
        # Find the next occurrence of the substring
        index = string.find(substring, index)

        # If we found an occurrence, increment the count and move the index forward
        if index!= -1:
            count += 1
            index += 1
        # If we didn't find an occurrence, break out of the loop
        else:
            break

    # Return the total count
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```