```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

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
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lowercase_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we first convert the input string to lowercase using the `lower()` method. This allows us to ignore case sensitivity and treat 'a' and 'A' as the same character.

We then use a set to store unique characters from the lowercase string. Sets in Python are unordered collections of unique elements, so any duplicate characters are automatically ignored.

Finally, we return the length of the set, which represents the number of distinct characters in the string.