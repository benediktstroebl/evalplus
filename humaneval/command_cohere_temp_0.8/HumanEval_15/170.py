```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
class TestStringSequence:
    def test_zero(self):
        assert string_sequence(0) == '0'

    def test_five(self):
        assert string_sequence(5) == '0 1 2 3 4 5'
```

The above code provides a self-contained Python script with a function `string_sequence(n)` that takes an integer `n` as input and returns a string containing space-separated numbers starting from 0 up to including `n`. It uses the `range()` and `map()` functions to generate numbers up to `n` and convert them to strings, and the `join()` method to concatenate these strings into one string with spaces in between.

The tests ensure that the function behaves as expected for values of `n` equal to 0 and 5. Certainly, feel free to add more tests to increase test coverage, such importance of maintaining good test coverage for robust code maintenance. Let me know if you would like to know more about testing in software development, and I'll be glad to elaborate!