```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Count overlapping cases.
    """ example: 'aaaaaa' contains 'aa' 3 times, returns 3.
    """
    input: "aaa", "a"
    """
    return len([x for x in string.findall(substring, string)])
```