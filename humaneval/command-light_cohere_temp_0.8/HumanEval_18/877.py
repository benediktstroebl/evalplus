Here is a self-contained Python script that defines a function how_many_times that finds the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'de')
    3
    >>> how_many_times('  abcdefg ', 'def')
    3
    """
    return len([i for i, j in enumerate(string.split(substring)) if string.split(substring)[0] == j])
```