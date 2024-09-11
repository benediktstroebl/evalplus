```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string to count distinct characters from

    Returns:
    int: The count of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # Use a set to store distinct characters, sets in Python are unordered collections of unique elements
    distinct_chars = set(string)
    # Return the count of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines the function `count_distinct_characters` and includes docstrings for documentation purposes. It utilizes the `lower()` function to convert the input string to lowercase, thus ignoring case sensitivity. Then it converts the string to a set, which automatically removes any duplicate characters. Finally, it returns the count of distinct characters by getting the length of the set.