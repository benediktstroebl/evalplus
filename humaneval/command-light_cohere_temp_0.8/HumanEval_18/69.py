Here is a self-contained Python function that solves the problem of counting the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    return len(string.find(substring))
```
This function uses the `find()` method to count the occurrences of the substring in the string, and returns the result.