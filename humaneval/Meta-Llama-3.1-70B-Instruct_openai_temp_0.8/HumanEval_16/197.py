```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to a set, which automatically removes duplicates
    # Use set comprehension to convert characters to lower case before adding to the set
    distinct_chars = {char.lower() for char in string}
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```