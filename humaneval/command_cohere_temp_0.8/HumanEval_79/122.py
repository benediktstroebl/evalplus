Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Outputs: db1111db
```

This script defines a function `decimal_to_binary` that takes a single argument, `decimal`, and converts it to its binary representation. It uses the `format` function with a binary format specifier (`{0:b}`) to convert the decimal number to a binary string. Finally, it prepends and appends "db" characters to the binary string to ensure the output matches the specified format. The example usage demonstrates how to use this function to convert the decimal number 15 to binary, and the output is "db1111db", as specified in the problem.