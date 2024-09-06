Here's a Python code block with a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation, with extra 'db' characters as specified in the problem:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return 'db' + binary + 'db'   # Add 'db' characters at the beginning and end

# Test Cases
decimal_numbers = [15, 32, 63, 45]
expected_results = ['db1111db', 'db100000db', 'db111111db', 'db01101db']

for dec, expected in zip(decimal_numbers, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected
```

This script includes a list of test cases (both decimal numbers and expected results) to ensure the function `decimal_to_binary` works correctly. You can use these test cases to verify the functionality of the function.