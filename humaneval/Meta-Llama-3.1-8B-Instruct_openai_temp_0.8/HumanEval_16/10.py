```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: Number of distinct characters in the string

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

In this script, we first convert the input string to lower case to ensure that the same characters in different cases are not counted as distinct characters. Then, we use a set to store unique characters in the string. Since sets in Python only store unique elements, the number of elements in the set represents the number of distinct characters in the string. Finally, we return the number of unique characters by getting the length of the set.