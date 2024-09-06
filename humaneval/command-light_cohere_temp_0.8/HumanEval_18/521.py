Here's the self-contained Python function that finds the number of times a given substring can be found in the original string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Calculates the number of times a substring appears in the original string.
    >>> how_many_times('aaaaaa', 'a') # Output: 6
    """
    count = 0
    start = 0
    length = len(substring)
    for i in range(len(string)):
        if string[i:i+length] == substring:
            start = i
            count += 1
    return count
```