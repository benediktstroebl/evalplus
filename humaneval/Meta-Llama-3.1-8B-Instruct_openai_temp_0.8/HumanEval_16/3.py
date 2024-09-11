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
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters and get the length of the set
    # A set in Python is an unordered collection of unique elements
    distinct_chars = set(string)
    
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, we define a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case sensitivity, and then uses a set to store unique characters. The length of the set is returned as the number of distinct characters. Finally, we test the function with the provided examples.