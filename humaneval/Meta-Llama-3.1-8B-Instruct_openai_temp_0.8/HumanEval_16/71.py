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
    return len(set(string.lower()))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, we use the `set` data structure in Python which contains unique elements. We convert the string to lowercase using the `lower()` method to ignore case sensitivity. The length of the set is then the number of distinct characters in the string.