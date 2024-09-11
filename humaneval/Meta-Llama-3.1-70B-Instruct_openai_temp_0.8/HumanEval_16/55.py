```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Args:
    string (str): The input string
    
    Returns:
    int: The number of distinct characters in the string
    
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to a set, which automatically removes duplicate characters
    # Convert the string to lower case to ignore case differences
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` which takes a string as input, converts it to lower case and then to a set. The set data structure in Python only stores unique elements, so this effectively removes any duplicate characters from the string. The function then returns the number of elements in the set, which is the number of distinct characters in the string.

The test cases at the end of the script demonstrate how to use the function and verify that it works as expected.