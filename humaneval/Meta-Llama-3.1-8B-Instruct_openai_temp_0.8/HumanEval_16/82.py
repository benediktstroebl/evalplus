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
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, as sets automatically remove duplicates
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters, which is the size of the set
    return len(unique_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase, stores unique characters in a set, and returns the number of unique characters. The test at the end demonstrates the function's usage.