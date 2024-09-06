```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

The `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `str` and `map` to convert these numbers into a space-delimited string. The `test_string_sequence` function provides test cases to validate the behavior of the `string_sequence` function. 

To run the test, the last line of the script calls the test function. The `assert` commands will automatically check the conditions and print out `True` if valid and `False` if there is an error and the test condition fails. 

Let me know if you would like me to make any modifications to the script or explain any particular piece of the code. 

You can also check out this [Python Documentation](https://docs.python.org/3/reference/expressions.html) for more information on the concepts used in the code such as `range`, `map`, and testing.