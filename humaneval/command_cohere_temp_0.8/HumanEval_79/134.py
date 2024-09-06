Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Output: db1111db
```

This script defines a function `decimal_to_binary` that takes a single argument, `decimal`, and converts it to its binary representation. It uses the `format` function with a specifier `b` to convert the decimal number to a binary string. Then, it returns the binary string encapsulated between 'db' characters at the beginning and end to ensure the desired format. The example usage demonstrates how to convert the decimal number 15 to binary (db1111db).