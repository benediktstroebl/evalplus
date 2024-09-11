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
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

This Python script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. The function works by first converting the string to lowercase, then converting it to a set, which automatically removes duplicates. The number of distinct characters is then returned as the length of the set.

The script also includes two test cases to verify the correctness of the function.