```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to ignore case differences
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets automatically eliminate duplicates.
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters, which is the size of the set.
    return len(unique_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case to ignore case differences, and uses a set to store unique characters. The function returns the number of unique characters, which is the size of the set. The script also includes test cases to verify the correctness of the function.