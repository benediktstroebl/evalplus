```python
def decimal_to_binary(decimal): 
    """
    Convert decimal number to binary format.
    :param decimal: str, the decimal number
    :return: binary string
    """
    # Convert decimal to binary
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary.  # Example string of binary digits, represented as '0' or '1' 
```
This Python function, `decimal_to_binary`, takes a single parameter, `decimal`, which is expected to be a string representing a decimal number. The function then converts the string to binary by repeatedly dividing the decimal number by 2 and storing the remainder in a string format.

The function then returns the resulting binary string.