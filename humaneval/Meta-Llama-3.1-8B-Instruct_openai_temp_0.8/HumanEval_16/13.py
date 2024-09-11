```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to make the comparison case-insensitive
    string = string.lower()
    
    # Use a set to store unique characters. Sets in Python are unordered collections of unique elements
    distinct_chars = set(string)
    
    # The number of distinct characters is the size of the set
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This script uses a Python set to store the unique characters in the string. Sets are unordered and automatically eliminate duplicates, so the size of the set is the number of distinct characters in the string. The function converts the string to lower case to make the comparison case-insensitive.