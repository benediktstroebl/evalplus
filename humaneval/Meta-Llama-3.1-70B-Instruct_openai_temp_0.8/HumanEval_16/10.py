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
    # Convert the string to a set of unique characters, ignoring case
    unique_chars = set(string.casefold())
    
    # Return the number of unique characters
    return len(unique_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines the function `count_distinct_characters` which takes a string as input and returns the number of distinct characters in the string, ignoring case. The `casefold()` method is used to convert the string to a case-insensitive format, and the `set()` function is used to remove duplicate characters. Finally, the `len()` function is used to count the number of unique characters.