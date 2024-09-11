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
    # Convert the string to lowercase to ignore case sensitivity
    lower_string = string.lower()
    
    # Use a set to store unique characters, sets automatically remove duplicates
    unique_chars = set(lower_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, ignoring case sensitivity. It uses a set to automatically remove duplicate characters and returns the length of the set, which represents the number of unique characters. The script includes examples to demonstrate its usage.