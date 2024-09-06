```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')  # [0, 3]
    >>> how_many_times('aaaa', 'aa')  # [3, 3]
    """
    return sum(1 for x in string.find(substring, 0, string. how.lower()) == substring.lower())

```