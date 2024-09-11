```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
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
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters, sets automatically eliminate duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script uses a `set` to store unique characters from the string, which automatically eliminates duplicates. It then returns the size of the set, which represents the number of distinct characters. The `lower()` method is used to convert the string to lowercase, ensuring the count is case-insensitive.