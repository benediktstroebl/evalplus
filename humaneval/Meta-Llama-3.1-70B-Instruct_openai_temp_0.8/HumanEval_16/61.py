```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use the set comprehension to create the set, and the lower() function to ignore case
    distinct_chars = {char.lower() for char in string if char.isalpha()}
    
    # The number of distinct characters is the size of the set
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines the `count_distinct_characters` function, which converts the input string to a set of distinct characters (ignoring case) and returns the size of this set. The function includes a docstring that explains its purpose, arguments, return value, and provides examples of usage. The script also includes test cases to verify the function's correctness.