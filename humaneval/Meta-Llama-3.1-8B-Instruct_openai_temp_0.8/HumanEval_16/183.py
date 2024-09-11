```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
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
        # Add the character to the set
        unique_chars.add(char)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script uses a set to keep track of the unique characters in the string. Sets in Python are unordered collections of unique elements. This makes them ideal for removing duplicates from a list or finding the number of unique elements in a list. In this case, we add each character to the set, and the set automatically removes any duplicates. The number of elements in the set is then returned as the number of unique characters. The `lower()` method is used to convert the string to lower case to ignore case sensitivity.