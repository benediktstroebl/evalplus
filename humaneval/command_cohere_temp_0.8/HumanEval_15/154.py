```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code snippet includes a function called `string_sequence` which takes an integer `n` as input and returns a string containing space-separated numbers ranging from 0 to `n` inclusive. The function uses the `range` function to generate numbers from 0 to `n` and then converts these numbers to strings using `str`, before joining them together with spaces using `join`.

The code then includes tests to verify the functionality of the `string_sequence` function. Firstly, it checks if the function returns '0' when `n` is 0. Secondly, it confirms that the function produces the expected output when `n` is 5. The expected output for `n` equal to 5 is '0 1 2 3 4 5'. These tests are performed using the `assert` statement, which verifies that the test conditions are true and raises an error if any of them are false.