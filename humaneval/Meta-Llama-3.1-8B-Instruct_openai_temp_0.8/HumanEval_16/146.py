```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to count distinct characters from

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case differences
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we first convert the input string to lowercase using the `lower()` method. This ensures that the same character in different cases is not counted as two distinct characters.

We then use a set to store unique characters. Sets in Python automatically eliminate duplicates, so the set `unique_chars` will contain only unique characters from the string.

Finally, we return the number of unique characters by getting the length of the set `unique_chars`.