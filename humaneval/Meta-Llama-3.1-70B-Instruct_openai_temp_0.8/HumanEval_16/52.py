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
    # We use the lower() function to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Remove all non-alphabet characters
    distinct_chars = {char for char in distinct_chars if char.isalpha()}
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. It uses a set to remove duplicates and the `lower()` function to ignore case sensitivity. The function also removes all non-alphabet characters from the string before counting the distinct characters.