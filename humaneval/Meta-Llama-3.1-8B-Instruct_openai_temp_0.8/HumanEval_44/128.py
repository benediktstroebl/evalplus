```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: Input number to be converted
    :param base: Target base for the conversion
    :return: String representation of the converted number
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))


# Example usage
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that performs the conversion from a decimal number to a specified base. It uses a while loop to continuously divide the input number by the target base and append the remainder to a list of digits. Once the loop finishes, it joins the digits list in reverse order to form the string representation of the converted number.