Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format"""
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Output: db1111db
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format. It uses the format specification character `b` to convert the decimal number to a binary string, and then adds "db" at the beginning and end of the string to conform to the specified format. The example usage demonstrates how to use the function to convert the decimal number 15 to binary format, resulting in the output "db1111db".