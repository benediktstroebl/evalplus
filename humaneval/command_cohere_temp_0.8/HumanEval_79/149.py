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

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Output: db100000db
```

This script defines a `decimal_to_binary` function that takes a decimal number as input and converts it to binary format. It uses the `format` method with a specification of `b` to directly convert the decimal number to a binary string. Finally, it prefaces and appends the binary string with "db" characters to meet the problem requirement. The script demonstrates its use with two examples, and the output prints the expected binary strings with the leading and trailing "db" characters.