Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # Removing '0b' from binary string
    return 'db' + bin_str + 'db'

# Test cases
decimal_values = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, result in zip(decimal_values, expected_results):
    assert decimal_to_binary(dec) == result
```

This script defines the `decimal_to_binary` function, which takes a decimal number as input and converts it to binary format. The function returns a string that starts and ends with 'db' to ensure consistent formatting. The provided test case demonstrates how the function behaves for different input values and asserts that the produced results match the expected binary representations.