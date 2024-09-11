```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    5
    """
    # Convert the string to lower case to handle case insensitivity
    string = string.lower()
    # Use a set to remove duplicate characters
    distinct_chars = set(string)
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

In this script, the `count_distinct_characters` function takes a string as input, converts it to lower case to handle case insensitivity, removes duplicate characters using a set, and returns the number of distinct characters. The function is then tested with the provided examples.