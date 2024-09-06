Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)
```
This function takes a decimal number `decimal` as input and converts it to its binary representation. It uses the `format` function with a binary prefix (`'b'`) to convert the decimal number to a binary string. Then, it returns the binary string wrapped in the prefix `'db'` at the beginning and end to ensure the desired output format with the extra characters.