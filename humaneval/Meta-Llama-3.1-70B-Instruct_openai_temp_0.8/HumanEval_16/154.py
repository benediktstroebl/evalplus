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
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    # Convert the string to a set, which automatically removes duplicate characters
    distinct_characters = set(lower_case_string)
    # Return the number of distinct characters
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case, and then converts it to a set. The set data structure automatically removes duplicate characters, so the number of elements in the set is the number of distinct characters in the original string. The function then returns this count. The script also includes two test cases to verify the function's correctness.