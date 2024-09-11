### Distinct Character Counter
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to handle case insensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets in Python are unordered collections of unique elements.
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it contains, regardless of case. It achieves this by converting the input string to lower case, using a set to store unique characters, and returning the length of the set. The test cases included demonstrate its usage.