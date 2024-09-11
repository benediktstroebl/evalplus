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
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters and get the count of elements in the set
    return len(set(string))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, the function `count_distinct_characters` works by first converting the input string to lower case to ignore case sensitivity. It then uses a set to store unique characters from the string. A set in Python is an unordered collection of unique elements. Therefore, a set automatically eliminates duplicate characters. Finally, the function returns the count of elements in the set, which is the number of distinct characters in the string.