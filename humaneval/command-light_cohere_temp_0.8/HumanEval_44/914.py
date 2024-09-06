```python
def change_base(x: int, base: int):
    """
    Change the base of integer x to base b, 
    and return the string representation.
    """
    for base in range(2, base=10):
        if x >= base:
            return '{:b}'.format(x // base)
        else:
            return '0'
    return 'Invalid base'

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(5, 5))  # Expected output: '05'
print(change_base(3, 2))  # Expected output: '0'
print(change_base(10, 10))  # Expected output: '10'
print(change_base(7, 5))  # Expected output: '571'
print(change_base(9, 3))  # Expected output: '8'
print(change_base(1234, 8))  # Expected output: '1000'
print(change_base(0, 7))  # Expected output: '0'
print(change_base(-1, 3))  # Expected output: 'Third Base'
```