```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicate characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Example usage
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5
```

This script works by first converting the input string to lower case, then converting it into a set. A set in Python is an unordered collection of unique elements, so any duplicate characters in the string are automatically removed. The number of distinct characters is then simply the size of the set, which is returned by the `len` function.