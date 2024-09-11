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
        4
    """
    # Convert the string to lowercase to make the function case-insensitive
    string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in that string. The function uses a set to remove duplicate characters and then returns the size of the set, which is the number of distinct characters. The script also includes example use cases at the end.