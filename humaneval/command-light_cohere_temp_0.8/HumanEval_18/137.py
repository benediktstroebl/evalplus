```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds the number of occurrences of a substring within the original string, 
    including overlapping substrings.
    """
    string = "Hello, hello world!"
    sub = "ll"
    occurrences = 0
    for char in string:
        if char == sub:
            occurrences += 1
    return occurrences
```