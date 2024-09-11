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
    string = string.lower()
    
    # Use a set to store unique characters, since sets automatically remove duplicates
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function with some examples
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case sensitivity, and then uses a set to store unique characters. It returns the number of unique characters by getting the length of the set. The examples at the end of the script demonstrate how to use this function.