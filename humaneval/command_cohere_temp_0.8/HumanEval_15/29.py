```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- This code utilizes the `range()` generator to generate numbers from 0 to `n`, and the `map()` function to convert these numbers to strings.
- The `join()` method is then used to concatenate these strings together with spaces in between. 

The tests included verify that the function behaves as expected for `n` values of 0, 5, and 10. 

To run the test, you can comment in the `test_string_sequence()` function and its calling statement if you haven't already.