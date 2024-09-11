```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function with some examples
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. We convert the string to lower case to ignore case sensitivity, then use a set to store unique characters. The number of unique characters is equal to the size of the set.