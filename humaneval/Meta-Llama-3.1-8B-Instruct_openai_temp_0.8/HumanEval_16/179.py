```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters does it consist of
    (regardless of case) """
    
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function uses a set to store unique characters, and the length of the set is returned as the number of distinct characters. The script also includes test cases to demonstrate the function's correctness.