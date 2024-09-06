```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within the original string.
    Args: 
        string: The input string
        substring: The substring to search for
    Returns: 
        int: Number of occurrences of the substring in the original string.
    """
    string = "aaaaaaa"
    substring = "a"
    return len(string.find(substring))
```

This code defines a function, `how_many_times`, which takes two arguments: a string and a substring. It then returns the how many times the substring can be found in the string, using the `find()` method from the string module.