```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)

# Test the function with provided examples
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This Python script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case to ignore case sensitivity, and uses a set to store unique characters. The function returns the number of unique characters in the string. Two test cases are provided to demonstrate the correct functionality of the function.