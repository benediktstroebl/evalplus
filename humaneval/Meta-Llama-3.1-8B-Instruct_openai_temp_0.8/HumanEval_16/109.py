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
    return len(set(string.casefold()))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this solution, we use the `casefold()` method to convert the input string to a case-insensitive format, and then convert it to a set. A set in Python is an unordered collection of unique elements, so the number of elements in the set is the number of distinct characters in the original string. We return the length of this set using `len()`.