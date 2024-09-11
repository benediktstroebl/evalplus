```python
# Define a function to count distinct characters in a string
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    Example:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_string = string.lower()
    
    # Use a set to store unique characters. Sets in Python are unordered collections of unique elements.
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_chars)

# Example usage
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. The function uses a set to store unique characters, which automatically removes duplicates. The size of the set is then returned as the number of distinct characters.