Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)

# Example usage:
decimal_value = 15
converted_value = decimal_to_binary(decimal_value)
print(f"Converted {decimal_value} to {converted_value}")
```
This script defines a function `decimal_to_binary` that takes a single argument, `decimal`, and returns the binary representation of that number with extra 'db' characters as specified in the problem statement. The built-in `format` function is used to convert the decimal number to a binary string, and then "db" is prepended and appended to create the desired format. The example usage demonstrates how to use this function to convert a decimal number to binary.