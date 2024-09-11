```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: Number of distinct characters

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    # Remove any non-alphabetic characters (like punctuation, digits, whitespace)
    cleaned_string = ''.join(filter(str.isalpha, lower_case_string))
    # Use a set to get distinct characters and return the size
    return len(set(cleaned_string))

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script accomplishes the task by first converting the input string to lowercase, then removing any non-alphabetic characters, and finally returning the size of the set of distinct characters.