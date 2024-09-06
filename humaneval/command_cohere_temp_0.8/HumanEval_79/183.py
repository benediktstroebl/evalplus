Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Returns a string representing the binary equivalent of the decimal number, with extra '0's and '1's for formatting."""
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{binary}db"
```

This script converts a given decimal number to a binary string with added leading and trailing characters 'db' to ensure a specific format. The `bin` function converts to binary, `replace` removes the '0b' prefix, and `rjust` ensures the binary string is the same length as the decimal number, with extra '0's for formatting. The final result ensures the binary string begins and ends with 'db'.