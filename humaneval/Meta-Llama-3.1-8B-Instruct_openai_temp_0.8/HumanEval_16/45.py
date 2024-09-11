```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_string = string.lower()
    
    # Use a set to store unique characters
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines the `count_distinct_characters` function, which converts the input string to lower case to ignore case sensitivity, stores unique characters in a set, and returns the number of distinct characters. The test cases at the end demonstrate the function's usage and expected output.