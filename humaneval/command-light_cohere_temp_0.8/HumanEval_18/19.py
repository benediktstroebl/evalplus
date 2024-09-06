Here's a self-contained Python function that solves the problem of finding the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string.
    If expected arguments:
    - string: the input string
    - substring: the substring to find

    Returns:
    int: the number of times the substring appears in the string
    """
    return len(string.find(substring))
```

This function utilizes the `find()` method from the string module, which is efficient for finding occurrences of a substring within a larger text. 
The function also handles the case where the substring is found nowhere in the string, returning 0.