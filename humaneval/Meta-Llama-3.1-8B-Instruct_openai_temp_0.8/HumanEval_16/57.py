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
    return len(set(string.casefold()))


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

In this script, the `count_distinct_characters` function converts the input string to lowercase using `casefold()` method, which is a case-insensitive version of the `lower()` method, and then converts it to a set. A set in Python is an unordered collection of unique elements, so the size of the set is the number of distinct characters in the string. The function returns the size of the set, which is the count of distinct characters.