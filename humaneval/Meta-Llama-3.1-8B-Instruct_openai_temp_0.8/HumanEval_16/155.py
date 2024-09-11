```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

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
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lowercase_string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. It uses a set to store unique characters, which automatically eliminates duplicates. The function converts the string to lowercase to ignore case sensitivity. The script also includes test cases to demonstrate the function's behavior.