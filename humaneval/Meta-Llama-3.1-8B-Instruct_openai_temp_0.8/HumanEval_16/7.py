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
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    distinct_characters = set(lowercase_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case sensitivity, stores unique characters in a set, and returns the number of distinct characters. The examples at the end demonstrate how to use the function.