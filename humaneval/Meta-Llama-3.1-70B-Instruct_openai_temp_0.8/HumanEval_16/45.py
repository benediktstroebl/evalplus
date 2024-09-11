```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Args:
    string (str): The input string.
    
    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to a set, which automatically removes duplicates
    # We also convert the string to lower case to make the comparison case-insensitive
    distinct_chars = set(string.lower())
    
    # The number of distinct characters is the size of the set
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aaa'))     # Expected output: 1
print(count_distinct_characters('aA'))      # Expected output: 1
print(count_distinct_characters('abcdef'))  # Expected output: 6
```