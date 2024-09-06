Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. Enjoy the script and let me know if you need anything else!
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal)), '0')
    return f"db{binary}db"
```