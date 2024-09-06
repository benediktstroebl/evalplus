Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided Markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)  # Output: db1111db

```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters added at the beginning and end for formatting purposes. The built-in `format` method is used to convert the decimal number to a binary string, and then the `format` function is used again to add the "db" characters at the beginning and end of the binary string.