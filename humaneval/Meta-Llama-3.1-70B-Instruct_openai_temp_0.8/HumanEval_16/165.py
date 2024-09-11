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

    # Convert the string to lowercase to ignore case sensitivity
    string_lower = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_chars = set(string_lower)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. The function works by converting the string to lowercase and then converting it to a set, which automatically removes duplicates. The length of the set is then returned as the number of distinct characters.