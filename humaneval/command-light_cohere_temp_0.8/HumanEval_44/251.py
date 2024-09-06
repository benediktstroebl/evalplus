```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Invalid input types. Input must be an numeric integer and base must be an integer.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    
    # Implements the conversion using the form of string representation for numbers
    return ''.format(int(str(x).format(format='{:0b}b')))

# Test cases
print(change_base(8, 3))        # Output: '22'
print(change_base(8, 2))       # Output: '1000'
print(change_base(7, 2))       # Output: '111'
print(change_base(127890, 2))   # Output: '234567890'
print(change_base(123, 3))     # Output: '12321'
print(change_base(123, 5))     # Should raise error: Invalid base value.
```