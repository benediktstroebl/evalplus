```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to count distinct characters from.

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
    
    # Use a set to store unique characters. Sets in Python only store unique elements.
    distinct_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script uses a set to store unique characters from the input string. It first converts the string to lower case to ignore case sensitivity, then it iterates over each character in the string and adds it to the set. Since sets only store unique elements, this effectively removes any duplicate characters. Finally, it returns the number of elements in the set, which represents the number of distinct characters in the string.