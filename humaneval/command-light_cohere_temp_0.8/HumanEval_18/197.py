```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a') == 3
    """
    counter = 0
    for i in range(len(string)):
        if string[i] == substring:
            counter += 1
    return counter
```