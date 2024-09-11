```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): Input string.

    Returns:
        int: Number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
print(count_distinct_characters('aaaAAA'))  # Expected output: 1
print(count_distinct_characters('abcde'))   # Expected output: 5
print(count_distinct_characters(''))        # Expected output: 0
```