```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets automatically eliminate duplicates.
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aaa'))     # Expected output: 1
print(count_distinct_characters('abcdef'))  # Expected output: 6
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function first converts the string to lower case to ignore case sensitivity. Then, it uses a set to store unique characters, which automatically eliminates duplicates. Finally, it returns the number of unique characters. The script also includes test cases to verify the correctness of the function.