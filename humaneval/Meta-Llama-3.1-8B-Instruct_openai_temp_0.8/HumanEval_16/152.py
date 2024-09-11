```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it consists of.

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case sensitivity, and uses a set to find the unique characters. The number of unique characters is then returned. The test cases at the end demonstrate the function's usage.