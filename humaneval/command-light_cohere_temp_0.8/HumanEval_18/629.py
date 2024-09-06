```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that counts the number of occurrences of a substring in the original string.
    >>> string = "aaaaaa"
    >>> substring = "a"
    >>> how_many_times(string, substring)
    ==> 3
    """
    count = 0
    length = len(string)
    for i in range(length):
        if string[i] == substring:
            count += 1
    return count
```