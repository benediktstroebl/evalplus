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

The above code provides a self-contained Python script that solves the problem with an example function and tests using the `unittest` framework. The `string_sequence` function creates a string of space-separated numbers starting from 0 and going up to including `n`. The `TestStringSequence` class has two test methods that check if the function behaves as expected for 0 and 5 as inputs. Adjust the inputs in the test methods to verify the behavior for other scenarios.