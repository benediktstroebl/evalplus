```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

To ensure the function is correct, two tests are added: one tests the edge case of n being 0, and the other tests the function with n being 5 to confirm that it outputs the correct string. 

The function itself uses Python's `range` to generate numbers up to including `n`, and then maps these to strings using `str`, separating them with spaces.