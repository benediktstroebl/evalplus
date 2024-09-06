Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)    # Convert decimal to binary and format result
    return "db{0}db".format(bin_str)     # Add extra characters 'db' at the beginning and end

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Output: db1111db (for decimal 15)

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Output: db100000db (for decimal 32)
```

This script incorporates the function `decimal_to_binary`, which accepts a decimal number as input and produces a string with the binary representation, encapsulated between extra characters 'db'. The `format` method is utilized to conform the binary string format and for the addition of the bounding 'db' characters. The example usage showcases the function's behavior when provided with different decimal numbers.