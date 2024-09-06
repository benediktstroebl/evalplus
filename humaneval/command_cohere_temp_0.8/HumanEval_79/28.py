Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This code snippet takes a decimal number, converts it to a binary representation using the `bin` function, and then appends the prefixes "db" at the beginning and end of the binary string to ensure the desired output format.