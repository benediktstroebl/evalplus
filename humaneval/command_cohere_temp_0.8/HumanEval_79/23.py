Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # strip '0b' from binary representation
    return 'db' + bin_str + 'db'

# Test Cases
decimal_values = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, result in zip(decimal_values, expected_results):
    assert decimal_to_binary(dec) == result
```

This script defines the `decimal_to_binary` function, which takes a decimal number as input and uses the built-in `bin` function to convert the decimal number to a binary string. The `[2:]` slice is used to remove the '0b' prefix from the binary string. The function then returns the binary string with the specified formatting, with 'db' characters added at the beginning and end.

The script then conducts a test using the `zip` function to check if the `decimal_to_binary` function is producing the expected outputs for the provided test cases.