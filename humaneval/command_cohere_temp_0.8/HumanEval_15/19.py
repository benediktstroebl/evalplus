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

The `string_sequence` function uses the `range` and `map` functions to generate numbers from 0 to `n` (`+ 1`) and convert them to strings, respectively. These strings are then joined together with spaces using the `join` method to produce the desired string sequence.

The `test_string_sequence` function creates an instance of the `unittest` module's `TestCase` class and adds test methods to it. Each test method, denoted by the `test_` prefix, contains an assertion to check the behavior of the `string_sequence` function with specific inputs. When the `run` method is called on the `TestCase` instance, these test methods are executed, and any assertions failures are reported.

To execute the test suite, the `test_string_sequence` function is called after the `string_sequence` function in the script. This way, the tests will be run whenever the script is executed.