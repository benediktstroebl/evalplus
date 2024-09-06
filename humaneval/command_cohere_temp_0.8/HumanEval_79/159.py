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

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```
This script includes the `decimal_to_binary` function that performs the conversion of the decimal number to a binary string, adding the leading 'db' and trailing 'db' as specified in the problem statement. The example provided demonstrates how to use the function to convert the decimal value of 15 to binary format, and the result is printed.