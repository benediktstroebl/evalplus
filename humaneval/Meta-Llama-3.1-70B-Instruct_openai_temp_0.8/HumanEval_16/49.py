```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): Input string.

    Returns:
        int: Number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to a set, which automatically removes duplicates
    # We also convert to lower case to make the comparison case-insensitive
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function works by converting the string to a set of lowercase characters, which automatically removes duplicates. The length of this set is then returned as the number of distinct characters. The script also includes test cases to verify that the function works correctly.