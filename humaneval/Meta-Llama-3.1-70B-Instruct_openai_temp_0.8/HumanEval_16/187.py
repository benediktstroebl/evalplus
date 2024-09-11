```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lower case to make the comparison case-insensitive
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicate characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. It first converts the string to lower case to make the comparison case-insensitive, then converts the string into a set, which automatically removes duplicate characters. Finally, it returns the number of distinct characters. The script also includes two test cases to verify the correctness of the function.