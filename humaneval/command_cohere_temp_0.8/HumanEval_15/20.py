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
- This code utilizes the `range()` generator to generate a list of numbers from 0 to `n`.
- The `map()` function is then used to convert these numbers to strings.
- The `join()` method is applied to concatenate the strings with spaces in between, thus forming the desired string sequence. 

The tests embedded in the code verify if the function `string_sequence` behaves as expected for various input values. 

To run the tests, you can execute the code directly in a Python environment or incorporate it into a larger test suite.