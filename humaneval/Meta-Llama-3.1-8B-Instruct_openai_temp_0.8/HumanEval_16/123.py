```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to get distinct characters, because sets in Python only store unique elements
    distinct_chars = set(lowercase_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script first converts the string to lower case to ignore case sensitivity. It then uses a set to get distinct characters. The `len()` function is used to get the number of elements in the set, which is the number of distinct characters.