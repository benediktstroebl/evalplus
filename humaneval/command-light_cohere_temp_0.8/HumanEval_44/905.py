```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base."""
    # Perform base conversion
    digits = [str(num) for num in str(x)]
    if base == 2:
        new_base = '10' if int(digits[0]) % 2 == 0 else '11'
        return f"{new_base}({digits[0]})"
    elif base == 10:
        return f"{digits[0]}{int(digits[1]) if digits[1] else ''}"
    else:
        raise ValueError("Invalid base number.")

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```
This code defines a function `change_base` that takes two parameters: `x`, which represents the number to be converted, and `base`, which represents the desired base to which the number should be converted to. They implement the specific logic based on the provided base number. The output is a string representation of the converted number.