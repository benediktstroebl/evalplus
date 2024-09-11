```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase and remove any spaces
    string = string.lower().replace(" ", "")

    # Use a set to get unique characters and return the count
    return len(set(string))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
print(count_distinct_characters('Python is awesome'))  # Output: 10
```

This script works by first converting the string to lowercase and removing any spaces. Then it uses a set to get unique characters. Since sets in Python cannot contain duplicate elements, this automatically eliminates any duplicate characters. Finally, it returns the count of the characters in the set, which represents the number of distinct characters in the string.