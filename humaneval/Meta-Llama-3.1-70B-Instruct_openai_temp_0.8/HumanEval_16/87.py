```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    5
    """
    # Convert the string to a set to remove duplicates, and to lower case to ignore case
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, the `count_distinct_characters` function takes a string as input and returns the number of distinct characters in the string. The `set` data structure is used to remove duplicates, and the `lower` method is used to convert the string to lower case to ignore case. The `len` function is then used to return the number of distinct characters.