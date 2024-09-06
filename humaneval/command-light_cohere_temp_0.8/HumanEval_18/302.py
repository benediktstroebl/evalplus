Here's a self-contained Python script with a function that finds the number of occurrences of a given substring within a given string, while avoiding the use of external tests and comments:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    6
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```