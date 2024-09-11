```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Parameters:
    string (str): The input string to find distinct characters in
    
    Returns:
    int: The number of distinct characters in the string
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Initialize an empty set to store unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set, which automatically removes duplicates
        unique_chars.add(char)
    
    # Return the number of unique characters (which is the size of the set)
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. It uses a set to automatically remove duplicate characters, making the process efficient even for large strings. The script includes docstrings and example use cases to explain the function's behavior and inputs/outputs.