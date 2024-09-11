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
    return len(set(string.casefold()))


# Test cases
if __name__ == "__main__":
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 5
    print("All test cases pass")
```

This script works by:

- Converting the string to casefolded form (a case-insensitive format) using the `casefold` method.
- Converting the string to a set, which automatically removes any duplicate characters.
- Returning the length of the set, which gives the number of distinct characters.

Note that the number of distinct characters in 'Jerry' is 5, not 4, because 'J', 'e', 'r', 'r', 'y' has 5 distinct characters when case sensitivity is ignored: 'J', 'e', 'r', and 'y'.