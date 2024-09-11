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
    # Convert the string to a set of characters after converting to lower case
    # A set automatically removes duplicates
    distinct_characters = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected: 3
print(count_distinct_characters('Jerry'))   # Expected: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it contains, regardless of case. The function works by converting the string to lower case and then to a set of characters, which automatically removes duplicates. The number of elements in the set is then returned.

The script also includes test cases to verify the correctness of the function.