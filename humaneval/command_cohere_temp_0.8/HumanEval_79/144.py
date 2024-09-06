Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)
```
This script provides a function called `decimal_to_binary` that takes a decimal number as input and converts it to a binary string. The `format` function is used to convert the decimal number to a binary string, where `0b` is prepended to the number, and `db` is appended to the end to maintain the specified format. The resultant binary string is then formatted with "db" at the beginning and end to produce the final output.