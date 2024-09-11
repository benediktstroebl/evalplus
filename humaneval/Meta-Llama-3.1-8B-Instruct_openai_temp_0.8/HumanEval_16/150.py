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
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # The number of distinct characters is the size of the set
    return len(unique_characters)


# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, the `count_distinct_characters` function takes a string as input, converts it to lowercase to ignore case sensitivity, and then uses a set to store unique characters. The number of distinct characters is simply the size of the set. The function returns this count.