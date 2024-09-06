```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    while ignoring case and avoiding duplicates.
    >>> string = "Hello World"
    >>> substring = "o"
    >>> how_many_times(string, substring)
    2
    >>> substring = 'll'
    >>> string = 'ELLO' 
    >>> how_many_times(string, substring)
    3
    >>> string = "aAA"
    >>> substring = "A"
    >>> how_many_times(string, substring)
    3
    """
    counter = 0
    for char in substring:
        if char in string and string.remove(char) != True:
            counter += 1
    return counter
```