```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to lower case to make the comparison case-insensitive
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets automatically eliminate duplicates.
    unique_characters = set(lower_case_string)
    
    # The number of distinct characters is the size of the set
    return len(unique_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aabbcc'))  # Expected output: 3
```