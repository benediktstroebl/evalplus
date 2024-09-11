```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case differences
    lowercase_string = string.lower()
    
    # Convert the lowercase string to a set, which automatically removes duplicates
    distinct_characters = set(lowercase_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines the `count_distinct_characters` function, which takes a string as input, converts it to lowercase to ignore case differences, converts it to a set to remove duplicates, and returns the size of the set, which represents the number of distinct characters in the string. The function is then tested with two example strings.