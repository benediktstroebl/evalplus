```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, since sets automatically eliminate duplicates
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters in the set
    return len(distinct_chars)

# Example usage
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, we first convert the input string to lowercase to ignore case sensitivity. Then, we use a `set` to store the unique characters. Finally, we return the number of distinct characters in the set using the `len` function. This solution has a time complexity of O(n), where n is the length of the input string, since set operations are generally O(n) in Python.