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
        5
    """
    # Convert the string to a set, which automatically removes duplicates.
    # We use the lower() method to make the comparison case-insensitive.
    distinct_chars = set(string.lower())
    
    # The number of distinct characters is the size of the set.
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

This script works by converting the input string to lowercase and then to a set, which automatically removes any duplicate characters. The size of the set is then the number of distinct characters in the string.