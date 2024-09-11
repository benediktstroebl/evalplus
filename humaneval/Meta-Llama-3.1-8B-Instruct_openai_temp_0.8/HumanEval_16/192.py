```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Convert the string to a set to remove duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case to ignore case sensitivity, and then converts it to a set to remove duplicates. The number of distinct characters is then returned as the length of the set. The script includes two test cases to demonstrate the function's behavior.