```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string.
    >>> print(how_many_times('abcdeabcdeda', 'abcd'))
    5
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```