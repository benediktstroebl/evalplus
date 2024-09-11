```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Parameters:
    string (str): The input string to count distinct characters from.
    
    Returns:
    int: The number of distinct characters in the string.
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function with example inputs
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script uses Python's built-in `set` data structure to efficiently remove duplicate characters. It first converts the input string to lowercase to ensure case-insensitive comparison. Then, it converts the string to a set, which automatically removes duplicates. Finally, it returns the number of distinct characters by taking the length of the set.