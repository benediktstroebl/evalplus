```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we define a function `count_distinct_characters` that takes a string as input. We first convert the string to lowercase using the `lower` method to ignore case sensitivity. Then, we use a `set` to store unique characters from the string. A `set` in Python is an unordered collection of unique elements. Therefore, when we add characters to a `set`, duplicates are automatically removed. Finally, we return the number of unique characters, which is the length of the `set`.