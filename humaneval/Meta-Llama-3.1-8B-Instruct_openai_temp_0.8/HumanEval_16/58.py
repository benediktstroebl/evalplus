```markdown
**Distinct Character Counter**
================================

This Python script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it consists of, ignoring case.

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string to count distinct characters from

    Returns:
        int: Number of distinct characters in the string

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case
    lower_case_string = string.lower()
    
    # Convert the string to a set to remove duplicates, then count the elements
    distinct_characters = len(set(lower_case_string))
    
    return distinct_characters

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script uses a set to remove duplicate characters and then counts the elements in the set to find the number of distinct characters. The string is converted to lowercase using the `lower()` method to ignore case.