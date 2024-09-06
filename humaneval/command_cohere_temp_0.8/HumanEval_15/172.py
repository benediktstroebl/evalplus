```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- This code utilizes the `range()` generator to produce a sequence of numbers ranging from 0 to `n`, inclusive.
- The `map()` function is used to convert these numbers to strings, appending a `1` to the end to account for the `n+1` range.
- The joined string is then returned as the result. 

The `test_string_sequence()` function is added to verify the correctness of the `string_sequence()` function. It checks for the return values against the expected outputs for `n` values of 0, 5, and 10.