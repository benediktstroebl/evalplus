```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): The input string
    
    Returns:
    int: Number of distinct characters in the string
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    5
    """
    return len(set(string.casefold()))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))    # Output: 5
```
This script defines a function `count_distinct_characters` that takes a string as an argument and returns the number of distinct characters (regardless of case) in the string. It uses Python's built-in `set` data structure, which automatically removes duplicates, and the `casefold` method, which converts the string to a case-insensitive format. The `len` function then returns the number of elements in the set, which is the number of distinct characters in the string.