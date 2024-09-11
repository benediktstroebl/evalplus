```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    """
    
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # The number of distinct characters is equal to the size of the set
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. It uses a set to store unique characters and then returns the size of the set, which represents the number of distinct characters.

The test cases at the end demonstrate the function's usage and expected output.