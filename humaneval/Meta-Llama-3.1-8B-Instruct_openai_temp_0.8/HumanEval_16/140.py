```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Parameters:
    string (str): The input string to count distinct characters from
    
    Returns:
    int: The number of distinct characters in the input string
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)


# Test the function with sample inputs
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. The function uses a set to store unique characters and returns the size of the set, which represents the number of distinct characters. The script also includes test cases to demonstrate the function's correctness.