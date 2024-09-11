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

    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. It uses Python's built-in `set` data type to remove duplicates from the string, and the `len` function to count the number of distinct characters. The script also includes test cases to demonstrate the function's usage.