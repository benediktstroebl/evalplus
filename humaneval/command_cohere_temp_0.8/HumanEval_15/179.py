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

The `string_sequence` function uses the `range` generator to generate numbers from 0 to `n`, and the `map` function to convert these numbers to strings with `str()`. It then uses `join()` to concatenate these strings with spaces in between. The `test_string_sequence` function provides test cases to validate the behavior of the `string_sequence` function. 

To run the test, save this code in a `.py` file and execute the file. The test will run automatically, and the result will be displayed on the console. If you encounter any issues, feel free to respond with additional details or specific errors you encounter, and I will be glad to assist you further!