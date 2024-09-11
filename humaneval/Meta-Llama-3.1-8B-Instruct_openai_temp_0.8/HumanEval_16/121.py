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
    
    # Use a set to store unique characters, sets automatically eliminate duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script works by first converting the input string to lowercase to ignore any differences caused by case. It then uses a set to store unique characters. Sets are a data type in Python that automatically eliminate duplicates, so the number of elements in the set is the number of distinct characters in the string. Finally, the script returns the size of the set, which is the number of distinct characters.