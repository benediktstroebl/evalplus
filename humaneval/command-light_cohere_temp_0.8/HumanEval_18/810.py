Here's a self-contained Python function that solves the given string splitting problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')    # 3
    >>> how_many_times('aaaaaaa', 'aa') # 5
    """
    return len(string.find(substring))
```
The function uses the `find()` method to search the substring in the original string and returns the length of the result.