```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base.
    The base numbers are 10, returns string representation.
    """
    return '{0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[(x // base) % base)]'
    """
    return [chr(int('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz[(x // base) % base)])][int(
        (base - 1) // 64
    )]

# Test cases
print(change_base(8, 2))        # Output: 1000
print(change_base(12, 35))       # Output: '1203'
print(change_base(65, 10))       # Output: '5'
print(change_base(35, 5))       # Output: '7'
print(change_base(10, 10))       # Output: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(change_base(22, 11))       # Output: '02221'
print(change_base(15, 13))       # Output: 'bb0aa'
```