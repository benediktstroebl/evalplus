Here's a Python script that defines a function to find the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  # Return 3
    >>> how_many_times('aaaa', 'aa')  # Return 3
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count
```