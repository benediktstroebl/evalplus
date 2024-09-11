```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to a set, which automatically removes duplicates
    # We also use case folding to ignore case differences
    distinct_chars = set(char.casefold() for char in string)
    
    # Remove any whitespace characters
    distinct_chars = {char for char in distinct_chars if not char.isspace()}
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('   abc  ')) # Expected output: 3
print(count_distinct_characters('aA'))      # Expected output: 1
print(count_distinct_characters('abcabc'))  # Expected output: 3
```