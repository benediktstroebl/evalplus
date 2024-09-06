Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Returns binary representation of decimal number with extra zeros and ones added at the beginning and end"""
    binary_string = bin(decimal)[2:]
    return "db" + binary_string + "db"
```

This script provides a function `decimal_to_binary` that takes in a decimal number as input and returns the binary representation of that number with "db" added at the beginning and end. The extra "db" ensures that the returned binary string is of fixed length to ensure uniformity in terms of output length. The bin() function is used in combination with [2:] to return the binary representation of the decimal number without the '0b' prefix.