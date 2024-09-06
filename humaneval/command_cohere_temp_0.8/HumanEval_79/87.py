Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided Markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Output: db1111db

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Output: db100000db
```

This script defines the `decimal_to_binary` function that takes a decimal number as input and converts it to binary format, adding 'db' characters as specified in the problem statement. The example usage demonstrates how to use the function to perform the conversion for different decimal numbers.