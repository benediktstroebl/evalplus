```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it consists of.

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
    # Convert the string to a set of distinct characters, ignoring case
    distinct_chars = set(string.casefold())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script works by first converting the input string to a set of distinct characters, ignoring case by using the `casefold()` method. The `casefold()` method is more aggressive than `lower()` in removing case distinctions, as it also takes care of some special cases like the German 'ß' character. The `set` data structure automatically removes any duplicate characters. The script then returns the length of this set, which is the number of distinct characters in the string.