```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to treat upper and lower case characters as the same
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script works by first converting the string to lowercase, then using a set to store unique characters. Sets automatically eliminate duplicates, and we can get the number of unique characters by getting the length of the set.