```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    >>> str.findall('substring', index) == -findall('string', 'substring')
    return 1 + how_many_times(string, substring[:index]) + how_many_times(string[index:], substring[index:])
    """
    return sum(1 for _ in string.findall(substring, string))
```