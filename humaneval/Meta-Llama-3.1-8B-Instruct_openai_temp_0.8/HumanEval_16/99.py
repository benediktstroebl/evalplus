```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case to ignore case sensitivity, removes duplicate characters using a `set`, and returns the number of distinct characters. The function is then tested with two example strings.