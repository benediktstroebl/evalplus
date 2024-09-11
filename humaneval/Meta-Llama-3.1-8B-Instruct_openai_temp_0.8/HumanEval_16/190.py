```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case differences
    string = string.lower()
    
    # Convert the string to a set to remove duplicates
    # A set in Python is an unordered collection of unique elements
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script uses the Python `set` data structure to remove duplicate characters from the string, effectively counting the number of distinct characters. The `lower()` method is used to convert the string to lowercase to ignore case differences. The function returns the length of the set, which represents the number of distinct characters.