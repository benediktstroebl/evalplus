```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

To guarantee the function can work with an integer `n` equal to 0, the inception of the range function has been included. When `n` is 0, the resulting string will contain only the number '0'. The test suite includes two additional test cases to confirm proper behavior for different input values.