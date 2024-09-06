Here's a self-contained Python script that defines a function to solve the problem you've described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    >>> how_many_times('aaa', 'a')
    3
    """
    return len([i for i, char in enumerate(string) if char == substring])

# Test cases
def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'a') == 4
    assert how_many_times('aaaaaa', 'aaa') == 6
test_how_many_times()
```
The `how_many_times` function uses a generator expression to count the occurrences of a given substring in the original string.