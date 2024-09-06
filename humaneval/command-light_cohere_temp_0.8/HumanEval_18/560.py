Here is a self-contained Python script that defines and implements a function to solve the given problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in a given string, considering overlapping substrings.
    >>> how_many_times('abcde', 'de')
    3
    """
    count = 0
    start = 0
    end = len(string) - 1
    while start <= end:
        if string[start:end] == substring:
            count += 1
        start += 1
        end -= 1
    return count
```