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
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. A set in Python is an unordered collection of unique elements.
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))
```

In this script, we first convert the input string to lower case to ignore case sensitivity. We then use a set to store unique characters. The `len()` function is used to get the number of elements in the set, which is the number of distinct characters in the string.