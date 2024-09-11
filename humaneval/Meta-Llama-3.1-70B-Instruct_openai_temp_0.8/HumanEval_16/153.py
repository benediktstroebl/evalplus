```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to set, which automatically removes duplicates
    # Then convert all characters to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```