Here's a Python code block with a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation according to the provided problem statement:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary representation."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary

# Test Cases
decimal_values = [15, 32, 64, 90]
expected_results = ['db1111db', 'db100000db', 'db1000000db', 'db1110102db']

for dec, expected in zip(decimal_values, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected, f"For decimal {dec}, expected {expected} but got {result}"
```

The function leverages Python's built-in `bin` function to convert the decimal number to its binary representation, and then performs some string manipulation to add the 'db' prefixes and suffixes as specified in the problem statement.

The test cases assert that the function's output for different decimal values matches the expected binary representations with the specified formatting.