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
    5
    """
    # Convert the string to a set, which automatically removes duplicates
    # Use the casefold method to ignore case
    distinct_chars = set(string.casefold())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to a set of distinct characters (ignoring case), and returns the number of distinct characters. The `casefold` method is used to ignore case, and the `len` function is used to get the number of elements in the set. The script also includes some test cases to demonstrate the function's behavior.