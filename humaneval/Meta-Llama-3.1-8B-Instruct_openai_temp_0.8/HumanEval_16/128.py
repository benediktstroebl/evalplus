```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to make the count case-insensitive
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets automatically eliminate duplicates
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function with example inputs
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. It uses the `lower` method to convert the string to lowercase, making the count case-insensitive. Then it uses a `set` to store unique characters, eliminating duplicates. Finally, it returns the number of distinct characters by getting the length of the set. The script also includes example inputs to test the function.