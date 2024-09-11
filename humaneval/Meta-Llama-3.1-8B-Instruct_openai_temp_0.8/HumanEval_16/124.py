```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to be processed

    Returns:
        int: The number of distinct characters

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_string = string.lower()
    
    # Initialize an empty set to store unique characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in lower_string:
        # Add the character to the set
        distinct_chars.add(char)
    
    # Return the number of distinct characters (size of the set)
    return len(distinct_chars)

# Test the function with example inputs
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case. The function uses a set to store unique characters and returns the size of the set, which represents the number of distinct characters. The script also includes example usage of the function with test inputs.