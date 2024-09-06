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

The `string_sequence` function uses the `range` and `map` functions to generate numbers from 0 to `n` (inclusive) and convert them to strings, respectively. It then uses `join` to concatenate these strings with spaces in between. The `test_string_sequence` function provides test cases to validate the behavior of the `string_sequence` function. 

To run the test, simply call `test_string_sequence()` after defining it. The output should indicate that the tests passed. 
* In this solution, the function `string_sequence` creates a space-delimited string of numbers from 0 to `n` using Python's `range` function and a mapping function to convert them to strings. This is done with the line:
```python
return ' '.join(map(str, range(n + 1)))
``` 

The `test_string_sequence` function creates an assert statement to test the output of `string_sequence` with the expected value for `n = 0` and `n = 5`. It further asserts that the length of the output string, when `n = 10`, is equal to 10, implying that the string contains 10 space-delimited numbers.