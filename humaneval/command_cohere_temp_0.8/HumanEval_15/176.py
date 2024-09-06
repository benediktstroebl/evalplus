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

The `string_sequence` function uses the `range` generator to generate numbers from 0 to `n`, and the `map` function to convert these numbers to strings with `str()`. It then uses `join()` to concatenate these strings with spaces in between, resulting in a string that represents the desired sequence of numbers. 

The `test_string_sequence` function verifies that the `string_sequence` function produces the expected outputs for various inputs. By using `assert` statements, it ensures that the actual outputs of the function match the expected outputs. Running this function executes the tests and provides feedback on whether the function is correct or not.  By having these tests, you can ensure that the `string_sequence` function is working correctly.  Thus, enabling you to catch any potential errors or unexpected behavior at an early stage.  This helps maintain the reliability and robustness of the code, especially when undergoing modifications or facing changes in requirements.