Here's a Python code block with a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation, with extra 'db' characters as specified in the problem statement:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b'
    return 'db' + binary + 'db'  # Add 'db' characters at the beginning and end
```

This function should be able to convert decimal numbers to binary formats as per the problem statement. For example, calling `decimal_to_binary(15)` would return `"db1111db"`, and calling `decimal_to_binary(32)` would return `"db100000db"`.