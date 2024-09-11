```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to count distinct characters from

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lowercased_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_characters = set(lowercased_string)
    
    # Return the number of unique characters
    return len(unique_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it consists of, regardless of case. The function works by first converting the input string to lowercase to ignore case sensitivity, then it uses a set to store unique characters and finally returns the number of unique characters. The script also includes test cases to verify the function's correctness.