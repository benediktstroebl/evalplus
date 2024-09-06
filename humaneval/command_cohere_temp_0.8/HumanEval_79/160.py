Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = '{:b}'.format(decimal)
    return 'db' + bin_str + 'db'

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Outputs: db1111db

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Outputs: db100000db
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format, as described in the problem statement. It uses the `format` method with a formatting specifier `{}` to convert the decimal number to a binary string, and then adds the prefix 'db' at the beginning and end of the string to ensure the desired output format. The function is demonstrated with test cases, where values of `decimal` are converted to binary format, and the expected output is produced.