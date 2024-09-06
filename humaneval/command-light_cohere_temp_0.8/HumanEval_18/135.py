```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string. 
    1.
    Example string: the string in which may contain the substring 
    2.
    substring: the substring to search for 
    Returns: the number of occurrences of the substring in the string
    """
    return len(string.find(substring))
```

This code provides a function, `how_many_times`, that takes two parameters: a string and a substring. It uses the `find()` function to search the substring within the original string and returns the number of occurrences of the substring in the string.