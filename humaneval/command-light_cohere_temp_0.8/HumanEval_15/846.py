```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {' and '.join(range(n+1, 0, -1))} "

# Test the function with various inputs
# Test case 1: Ensure it works with negative numbers also
test_string_sequence = lambda : assert_eq(string_sequence(-5),'0 -4 -3 -2 -1')
test_string_sequence()

# Test case 2: Test with large n values
test_string_sequence = lambda : assert_eq(string_sequence(10000),'0 1000000')
test_string_sequence()

# Test case 3: Test with varying n values
test_string_sequence = lambda : assert_eq(string_sequence(8),'0 8')
test_string_sequence()

# Test case 4: Validate the length of output
test_string_sequence = lambda : assert_eq(len(string_sequence(8)),len('08')),
test_string_sequence()
```

This Python script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-separated numbers from 0 to `n`, including the endpoints. It is run several tests to validate the correctness of the function. This script is also an set of tests that cover various scenarios for the `string_sequence` function.