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
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_chars = set(string)
    
    # Return the number of unique characters, which is the size of the set
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script does the following:

1. Converts the input string to lowercase using the `lower()` method to ignore case sensitivity.
2. Creates a set (`unique_chars`) from the lowercase string. Sets in Python automatically eliminate duplicates.
3. Returns the number of unique characters by getting the size of the set using the `len()` function.

The `set` data structure is used here because it provides efficient membership testing and eliminates duplicates automatically, making it ideal for this problem.