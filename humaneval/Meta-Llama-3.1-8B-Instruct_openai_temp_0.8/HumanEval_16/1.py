```python
def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to handle case-insensitivity
    lower_case_string = string.lower()
    
    # Create a set from the string which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

However, this can be simplified even more using Python's built-in `set` and `lower()` functions.

```python
def count_distinct_characters(string: str) -> int:
    """Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to a set of lowercase characters and return its length
    return len(set(string.lower()))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This version of the function achieves the same result as the original one but in a more concise way.