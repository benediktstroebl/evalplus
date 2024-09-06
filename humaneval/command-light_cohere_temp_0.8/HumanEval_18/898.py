Here's the self-contained Python script that defines and tests a function that finds the number of occurrences of a given substring within a given string:
```python
import string
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    >>> string = 'aaaaaa'
    >>> substring = 'a'
    >>> how_many_times(string, substring)
    3
    >>> string = 'hello'
    >>> substring = 'world'
    >>> how_many_times(string, substring)
    0
    >>> string = 'hello world'
    >>> substring = 'oow'
    >>> how_many_times(string, substring)
    2
    """
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count
```