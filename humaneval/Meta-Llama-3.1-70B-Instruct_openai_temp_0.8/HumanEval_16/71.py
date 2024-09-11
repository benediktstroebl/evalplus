```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it consists of.

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
    # Convert the string to a set, which automatically removes duplicates
    # We convert the string to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. The function works by converting the string to a set, which automatically removes duplicates, and then returning the size of the set. We convert the string to lower case before creating the set to ensure that the function is case-insensitive. The script also includes some test cases to verify that the function works correctly.