Here's a Python code block with a function `decimal_to_binary` that completes the described task:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return f"db{binary}db"
```

This approach converts the decimal number to its binary representation using the `bin` function and slices off the leading '0b' and trailing null character. It then prepends and appends 'db' to ensure the result is a string with the desired format.