```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): The input string
    
    Returns:
    int: The number of distinct characters in the string
    """
    # Convert the string to lower case to make the comparison case-insensitive
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets in Python cannot have duplicate values.
    unique_chars = set(lower_case_string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function uses the `lower()` method to convert the string to lower case, and the `set` data structure to store unique characters. The test cases at the end of the script verify the function's correctness.