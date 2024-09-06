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

This script defines the `decimal_to_binary` function, which takes a decimal number as input and converts it to its binary representation. The conversion is done using a while loop that keeps dividing the input by 2 and storing the remainder as bits in reverse order. The resulting binary string is then padded with 'db' characters at the beginning and end to ensure the required format.

The script also includes test cases to validate the correctness of the `decimal_to_binary` function. You can use these test cases to verify other decimal numbers as well, ensuring the function behaves as expected.