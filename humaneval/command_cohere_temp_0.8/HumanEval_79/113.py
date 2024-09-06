Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    bin_str = '{0:b}'.format(decimal)    # Convert decimal to binary and prefix with '0b'
    return 'db' + bin_str + 'db'           # Add 'db' prefixes and suffixes for better alignment

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Outputs: db1111db (for decimal 15)
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with appropriate prefixes and suffixes for formatting. The `format` method is used to convert the decimal number to a binary string, and then the 'db' prefixes and suffixes are added for better alignment of the binary digits.