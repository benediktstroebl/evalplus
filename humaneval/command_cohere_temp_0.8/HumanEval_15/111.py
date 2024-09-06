```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive.
    """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
import pytest

@pytest.mark.parametrize('n, expected', [
    (0, '0'),
    (5, '0 1 2 3 4 5')
])
def test_string_sequence(n, expected):
    actual = string_sequence(n)
    assert actual == expected
```

This script includes a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-separated numbers ranging from 0 to `n` (inclusive) when `n` is greater than 0. If `n` is 0, it returns '0'. 

It uses the `range` function to generate a sequence of numbers from 0 to `n` and then uses `str` and `map` functions to convert these numbers into a space-separated string. The `join` method is then used to concatenate the strings into a single string. 

It also includes a unit test using the `pytest` framework. This test checks whether the `string_sequence` function produces the correct output for various inputs (`n`) by comparing the output to the expected value.