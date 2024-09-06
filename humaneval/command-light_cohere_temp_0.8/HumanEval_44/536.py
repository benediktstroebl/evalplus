```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base.
    return string representation after conversion.

    base numbers are universal (base > 2)
    """
    if base <= 1 or base > 36:
        raise ValueError("Invalid base number")
    return f"{x:{base}}" if isinstance(x, str) else f'{x:{base}}'

# Unit tests
print(change_base(8, 3))      # Expected output: '22'
print(change_base(123, 45))    # Expected output: '5305'
print(change_base(5, 60))     # Expected output: '60'
print(change_base(123.4567, 2))  # Expected output: '4567'
```
The code defines a function `change_base` that converts a number to a string representation using a specified base. It also raises a specific exceptions for invalid base numbers and performs unit tests to verify its functionality.