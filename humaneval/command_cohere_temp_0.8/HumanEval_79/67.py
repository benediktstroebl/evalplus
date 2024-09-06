Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_string = str(remainder) + binary_string
    binary_string = 'db' + binary_string + 'db'
    return binary_string

# Test Cases
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(32) == 'db100000db'
```
This script defines the `decimal_to_binary` function, which takes a decimal number as input and converts it to its binary representation. The binary representation is encapsulated within the characters 'db' at the beginning and end to ensure the desired format. Subsequently, the function returns the formatted binary string.

The test cases are also correctly formatted, with each test case exercising a different decimal input and asserting the corresponding expected output.