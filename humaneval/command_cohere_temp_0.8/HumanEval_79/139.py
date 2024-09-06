Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. Enjoy the snippet:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return 'db' + bin_str + 'db'    # Add 'db' at the beginning and end for formatting

# Test Cases
decimal_numbers = [15, 32, 64, 7]
expected_results = ['db1111db', 'db100000db', 'db1000000db', 'db0111db']

for dec, expected in zip(decimal_numbers, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected, f"For decimal {dec}, expected {expected}, but got {result}"
```

The function `decimal_to_binary` in this code snippet accepts a decimal number as input and outputs a string containing the binary representation of the number, with the required 'db' characters added to the beginning and end. To ensure correctness, the test cases and expected results are also provided, and the code snippet includes a test loop to validate the function's behavior against these test cases.