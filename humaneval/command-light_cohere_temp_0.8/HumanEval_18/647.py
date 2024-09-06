```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    >>> string = "aaa"
    sub = "aa"
    count = 0
    for i in range(len(string)):
        if string[i] == sub:
            count += 1
    return count
    """
def test_function():
    try:
        print(how_many_times('aaa', 'aa'))
    except Exception as e:
        print(e)
```