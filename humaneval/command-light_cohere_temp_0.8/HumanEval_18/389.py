Here's a self-contained Python script that defines a function `how_many_times` that calculates the number of times a given substring can be found in another string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Count how many times a given substring can be found in the original string.

    Count case of substring can be found if it is present at any position in the original string.

    For example:
    >>> how_many_times('aaaaaa', 'aa')
    3
    >>> how_many_times('hello world', 'o')
    0
    """
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count
```