```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    # Handle edge cases where either string is empty
    if not substring:
        return 0

    # Initialize a counter to store the number of occurrences
    count = 0

    # Iterate over the string, considering substrings of the same length as the target substring
    for i in range(len(string) - len(substring) + 1):
        # Check if the current substring matches the target substring
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1

    # Return the total count of occurrences
    return count

# Example use cases:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

Alternatively, you can use Python's built-in `str.find()` method to achieve the same result in a more concise way:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

# Example use cases:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```