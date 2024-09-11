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
    
    # Convert the string to a set, which removes duplicate characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines the `count_distinct_characters` function, which first converts the input string to lower case to ignore case differences. It then converts the string to a set, which automatically removes any duplicate characters. Finally, it returns the number of distinct characters by getting the length of the set.

The script also includes two test cases to verify that the function works correctly.