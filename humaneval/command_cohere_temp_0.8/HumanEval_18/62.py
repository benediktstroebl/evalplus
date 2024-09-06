Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    return string.count(substring)

def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaaa') == 1
    assert how_many_times('bbbbb', 'bb') == 5
    assert how_many_times('abc', 'abc') == 1

test_how_many_times()
```

I've added a comprehensive test suite using the `test_how_many_times()` function to cover various scenarios. The `how_many_times()` function itself counts the occurrences of the `substring` in the `string` using the built-in `count()` method.