```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to handle case-insensitivity
    string = string.lower()
    
    # Initialize an empty set to store unique characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        distinct_chars.add(char)
    
    # Return the number of distinct characters (which is the size of the set)
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, we use a set to store unique characters. Sets in Python are unordered collections of unique elements. This property makes it ideal for storing distinct characters. We iterate over each character in the string, add it to the set, and then return the size of the set, which represents the number of distinct characters. We also handle case-insensitivity by converting the string to lowercase before processing.