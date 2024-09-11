```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string to count distinct characters from.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to handle case-insensitive comparison
    string_lower = string.lower()
    
    # Convert the string to a set to remove duplicates
    distinct_chars = set(string_lower)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, we first convert the input string to lowercase using the `lower()` method to handle case-insensitive comparison. Then we convert the string to a set using the `set()` function, which automatically removes any duplicate characters. Finally, we return the length of the set, which gives us the number of distinct characters in the string.