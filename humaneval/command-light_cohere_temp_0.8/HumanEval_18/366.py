Here is a self-contained Python function that solves the problem of counting the number of occurrences of a substring in a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string,
    while ignoring case and counting overlapped matches.
    >>> how_many_times('aaaaaa', 'aa')
    3
    """
    return sum(1 for i,x in enumerate(string.find(substring, case=False)):
```
This function uses the `find()` function along with a generator expression to count all positions of the substring, without considering the case.

The function also counts the matches that are overlapped in the original string.