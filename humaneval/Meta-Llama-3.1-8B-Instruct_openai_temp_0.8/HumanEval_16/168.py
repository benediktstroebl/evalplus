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
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, we first convert the input string to lower case using the `lower()` method to ignore case sensitivity. Then, we use a set to store unique characters from the string. Since sets automatically eliminate duplicates, we can get the number of distinct characters by getting the size of the set using the `len()` function.