```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters. Sets in Python are unordered collections of unique elements.
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, the `count_distinct_characters` function works by first converting the input string to lower case. This is to ensure that the function counts 'a' and 'A' as the same character.

Then, it uses a set to store unique characters from the string. Sets in Python are unordered collections of unique elements. This means that if we try to add a character that is already in the set, it will be ignored.

Finally, the function returns the number of unique characters in the set, which is the count of distinct characters in the input string.