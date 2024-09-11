```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    return len(set(char.lower() for char in string))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Should print: 3
print(count_distinct_characters('Jerry'))   # Should print: 4
```

In this code, we use the `set` data structure to remove duplicate characters. The `char.lower()` function is used to convert all characters to lowercase, so that the same characters in different cases are not counted as distinct. The `len` function then returns the number of distinct characters.