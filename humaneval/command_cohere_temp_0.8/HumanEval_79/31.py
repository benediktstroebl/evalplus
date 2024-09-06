Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary_string = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_string = str(remainder) + binary_string
    binary_string = 'db' + binary_string + 'db'
    return binary_string
```
This function iteratively converts the decimal number into a binary string, with each iteration representing a digit in the binary format. The `str(remainder)` is used to convert the binary digit (0 or 1) to a string representation, and empty strings are prepended and appended with 'db' to maintain the specified output format.