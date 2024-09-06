```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
class TestStringSequence:
    def test_zero(self):
        assert string_sequence(0) == '0'

    def test_five(self):
        assert string_sequence(5) == '0 1 2 3 4 5'
```

The above code provides a function `string_sequence` that takes in a integer `n` and returns a string consisting of space-delimited numbers starting from 0 up to `n` inclusive. The code also includes tests that verify the function works correctly for 0 and 5.