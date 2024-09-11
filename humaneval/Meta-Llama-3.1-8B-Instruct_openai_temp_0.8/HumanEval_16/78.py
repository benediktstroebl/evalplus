```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: Number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # Use a set to store unique characters and return the count of the set
    return len(set(string))

# Test the function with provided examples
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

In this script, the function `count_distinct_characters` takes a string as input, converts it to lowercase to ignore case sensitivity, and uses a set to store unique characters. Since sets automatically eliminate duplicates, the length of the set will be the number of distinct characters in the string. This count is then returned as the result.