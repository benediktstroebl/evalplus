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
    string = string.lower()
    
    # Use a set to store unique characters, which automatically ignores duplicates
    unique_chars = set(string)
    
    # Return the number of unique characters, which is the size of the set
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script uses a Python set to store unique characters from the input string, which automatically ignores duplicates. The size of the set is then returned, giving the total number of distinct characters in the string. The `lower()` method is used to convert the string to lowercase, ensuring that the function is case-insensitive.