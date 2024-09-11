```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to a set of characters, which automatically removes duplicates.
    # We use the lower() method to make the comparison case-insensitive.
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters, which is the size of the set.
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to a set of distinct characters (case-insensitive), and returns the size of the set. The test cases are included at the end to verify the functionality of the function.