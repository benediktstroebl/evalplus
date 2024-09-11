### Distinct Characters Counter
#### A Python Function to Count Distinct Characters in a String

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # Use a set to store unique characters, since sets in Python cannot contain duplicate values
    distinct_chars = set(string)
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. The function converts the string to lowercase to ignore case sensitivity, then uses a set to store unique characters. The number of distinct characters is returned as the length of the set.