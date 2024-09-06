Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"
```
This Python function takes a decimal number as input and converts it to its binary representation, with extra characters 'db' added at the beginning and end of the string for formatting purposes. The binary string is generated using the `bin` function, and then appended with the 'db' characters before returning the final string.