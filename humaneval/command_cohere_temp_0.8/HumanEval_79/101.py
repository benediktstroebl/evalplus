Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join(str(x) for x in bins) + 'db'

# Test cases
decimal_values = [15, 32, 64, 7]
expected_results = ['db1111db', 'db1000000db', 'db100100100db', 'db0111db']

for dec, expected in zip(decimal_values, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format, according to the specification you provided. It then includes a test suite with a list of test cases and expected outputs. The `zip` function is used to iterate over each test case and expected result simultaneously. The `decimal_to_binary` function is called for each test case, and the result is compared to the expected output using the `assert` statement, which ensures that the code behaves as expected.  If the test cases pass, the code will not produce an error and will proceed to the next test case.