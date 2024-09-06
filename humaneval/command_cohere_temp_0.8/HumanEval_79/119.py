Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = ''
    while decimal > 0:
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2
    return 'db' + binary_string + 'db'

# Test cases
decimal_15 = decimal_to_binary(15)
decimal_32 = decimal_to_binary(32)

print(decimal_15 == 'db1111db')
print(decimal_32 == 'db100000db')
```
This script includes the `decimal_to_binary` function that performs the conversion of a decimal number to its binary representation. It iterates through the decimal value, keeping track of the remainder when divided by 2. The binary string is built from these remainders, surrounded by 'db' at the start and end to ensure the desired format. The test cases validate the correctness of the function's behavior for the given examples.