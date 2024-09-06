Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format with extra 'db' characters."""
    binary = f"db{bin(decimal)[2:]}.strip('b') + 'db'"
    return binary
```

This script provides a function that takes in a decimal number and converts it into a binary string according to the given problem statement. It uses the `bin` function to convert the decimal number to a binary string, then adds 'db' extra characters at the beginning and end of the string. The `f-string` and `.strip('b')` method are used for simplicity and readability.