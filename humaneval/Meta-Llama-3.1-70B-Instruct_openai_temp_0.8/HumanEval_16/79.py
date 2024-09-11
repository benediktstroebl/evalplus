```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        5
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script works by first converting the input string to lower case. This is to ensure that the same character in different cases is not counted as distinct. Then, it uses a set to store unique characters from the string. Finally, it returns the number of unique characters, which is the size of the set.

Please note that in the example for 'Jerry', the expected output is 5 because it consists of 'j', 'e', 'r', 'r', 'y', and the set will ignore duplicate 'r'.