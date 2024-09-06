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

This code snippet defines the function `decimal_to_binary(decimal)` which takes a single argument, `decimal`, and returns the binary representation of that number with extra 'db' characters at the beginning and end. The function uses a while loop to iterate through the digits of the decimal number, converting each digit to its binary representation and building the binary string. The test cases assert that the function produces the correct binary representations for the given decimal numbers.