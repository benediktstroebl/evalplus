```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string, 
    without overlapping.
    """
    start = 0
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
        if count > 1:
            return i
    return -1
```