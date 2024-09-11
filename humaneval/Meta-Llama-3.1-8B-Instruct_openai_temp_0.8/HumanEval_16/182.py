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
    return len(set(string.casefold()))


# Example use case:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
print(count_distinct_characters('Hello World'))  # Output: 10
```

In this script, the `casefold()` method is used to convert the string to a case-insensitive format. The `set()` function then creates a set of unique characters from the string, and the `len()` function returns the number of elements in this set, which is the number of distinct characters.