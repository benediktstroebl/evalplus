Here is a self-contained Python script that defines a function how_many_times that finds the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    6
    """
    return len([x for x in string.match(substring)]
```

This script provides a function that takes two parameters: a string and a substring. It uses the matchedel string's substring within the original string using the `match()` function and then returns the length of the matched substring.