Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)
```
This function takes a decimal number as its input and returns a string in binary format. The `format` function is used to convert the decimal number to a binary string, where `0b` is prepended and `b` is appended to complete the binary representation. The overall process is encapsulated with the function that delivers the expected results.