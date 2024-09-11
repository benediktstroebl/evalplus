### Distinct Characters Counter
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. It uses a set to store unique characters, which automatically removes duplicates. The function first converts the string to lowercase, and then uses a set to count the number of distinct characters. The result is returned as an integer. The script includes test cases to demonstrate the function's correctness.