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
        5
    """
    # Convert the string to a set, which automatically removes duplicates.
    # We use a set comprehension to convert each character to lower case before adding it to the set.
    distinct_characters = {char.lower() for char in string}
    
    # The number of distinct characters is the size of the set.
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

This script uses a set to store the distinct characters in the string. Since sets in Python cannot contain duplicate values, this automatically removes any duplicate characters. The `lower()` method is used to convert each character to lower case before adding it to the set, so that the same character in different cases is not counted as multiple distinct characters. The `len()` function is then used to get the number of distinct characters, which is the size of the set.