```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to a set, which automatically removes duplicates
    # Convert to lower case to ignore case differences
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case differences. It uses a set to remove duplicates and then returns the size of the set. The test cases at the end demonstrate the function's correctness.