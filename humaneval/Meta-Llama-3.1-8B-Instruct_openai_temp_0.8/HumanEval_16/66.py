```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Parameters:
    string (str): The input string
    
    Returns:
    int: The number of distinct characters in the string
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets in Python automatically eliminate duplicates.
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Should print 3
print(count_distinct_characters('Jerry'))   # Should print 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case. It uses a set to store unique characters, and returns the size of the set as the result. The function is then tested with two example inputs.