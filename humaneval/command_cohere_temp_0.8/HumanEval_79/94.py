Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra '0's and '1's at the start and end:
```python
def decimal_to_binary(decimal):
    """
    Convert a decimal number to binary format.
    """
    binary = bin(decimal).replace('0b', 'db').replace('{}'.format, 'db')
    return binary
```

In this code, the `decimal_to_binary` function takes a decimal number as input. The binary representation of the input number is found using the `bin` function. The `replace` function is used to replace the `0b` prefix with `db` to achieve the desired output format. Similarly, `db` is appended at the end to ensure the desired output format is achieved.