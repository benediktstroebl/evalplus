```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to calculate distinct characters from.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters. Sets in Python are unordered collections of unique elements.
    unique_chars = set(string)
    
    # The number of distinct characters is the size of the set
    return len(unique_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. It first converts the string to lowercase to ignore case sensitivity, then uses a set to store unique characters and returns the size of the set. The script also includes example use cases to demonstrate the function's behavior.