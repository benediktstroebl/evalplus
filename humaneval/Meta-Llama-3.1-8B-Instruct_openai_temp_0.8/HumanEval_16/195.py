```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as an input, converts it to lowercase, stores its unique characters in a set, and returns the size of the set, which represents the number of distinct characters. The test cases at the end demonstrate how to use this function and verify its correctness.