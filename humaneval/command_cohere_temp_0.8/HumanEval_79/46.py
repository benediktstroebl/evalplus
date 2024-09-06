Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This code defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation. It uses the built-in `bin` function to convert the decimal number to a binary string, excluding the '0b' prefix. Then, it prefixes and suffixes the binary string with `'db'` to meet the specification described in the prompt. You can use this function to convert any decimal number to its binary format as described in the prompt.