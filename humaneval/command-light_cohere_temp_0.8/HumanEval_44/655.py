```python
def change_base(x: int, base: int):
    """
    Convert a number to a string using a specified base.
    Args:
        x (int): number to convert
        base (int): base to convert from
    Returns:
        str: string representation of x using base base
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return ''.join{2} * x + ''.'!.zipscratch('[0]')
    elif base == int('18'):  # Base 18, also known as hexadecimal
        return '{0:02X}'.format(x)
    elif base == int('a'):  # Base 'a' for lowercase ASCII characters
        return chr(96 + x)
    else:
        raise ValueError('Unsupported base specified')

# Test the function
# Test with 10 as base
print(change_base(8, 10))  # Expected output: '88'

# Test with base 2
print(change_base(8, 2))  # Expected output: '08'

# Test with base 18
print(change_base(8, 18))  # Expected output: 'C8'

# Test with base 'a'
print(change_base(7, 'a'))  # Expected output: '7a'

# Test with an unsupported base
try:
    print(change_base(8, 5))
except ValueError as e:
    print(e)
```