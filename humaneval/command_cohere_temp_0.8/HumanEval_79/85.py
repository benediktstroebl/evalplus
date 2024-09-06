Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes corresponding tests:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = "{0:b}".format(decimal)    # Convert decimal to binary and prefix with '0b'
    return "db"+bin_str+"db"              # Add 'db' characters at the beginning and end

# Example usage:
decimal_val = 15
result = decimal_to_binary(decimal_val)
print(result)  # Output: "db1111db"

decimal_val = 32
result = decimal_to_binary(decimal_val)
print(result)  # Output: "db100000db"
```

The provided example usage demonstrates how to call the `decimal_to_binary` function with different input values (`15` and `32`) and print the resulting binary strings with the leading and trailing `db` characters. The function uses the format specification `{0:b}"` to convert the decimal number to a binary string, and then adds the necessary leading and trailing characters for the desired output format.