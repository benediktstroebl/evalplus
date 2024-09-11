```python
def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

This script defines the `count_distinct_characters` function, which takes a string as input and returns the number of distinct characters it contains. It converts the string to lowercase to ignore case sensitivity, uses a set to store unique characters, and returns the size of the set as the result. The script includes example test cases to demonstrate the function's usage.