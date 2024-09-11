```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use a case-insensitive approach by converting the string to lower case
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```