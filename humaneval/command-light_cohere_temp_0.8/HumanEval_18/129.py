```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, without overlapping.
    >>> string = 'aaaaaaa tree cone good'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    3
    >>> string = 'aaaaaaa tree original value'
    >>> substring = 'o'
    >>> how_many_times(string, substring)
    0
    >>> string = 'abcdeabcfdsa'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```