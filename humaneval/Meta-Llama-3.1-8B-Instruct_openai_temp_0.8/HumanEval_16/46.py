```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    
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
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)

# Test the function with some examples
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This Python script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it contains, regardless of case. It uses a set to store unique characters, which automatically eliminates duplicates. The function is then tested with some examples.