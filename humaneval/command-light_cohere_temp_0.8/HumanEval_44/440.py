```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    # Use a generator expression to reverse the digits in x with the base
    s = str(x)
    reversed_s = ''.join(reversed(s))
    return format(int(reversed_s), f"{base}EIN")

# Basic tests
print(change_base(8, 3))  # Expected output: '22'
print(change_base(123, 2))  # Expected output: '2321'
print(change_base(123, 10))  # Expected output: '111222333'
print(change_base(123, 20))  # Expected output: '12345678'
print(change_base(123, 21))  # Expected output: Error: ValueError: Invalid base number.

# Edge cases
print(change_base(123, 1))  # Expected output: Error
print(change_base(-123, 10))  # Expected output: Error
print(change_base(1, 57))  # Expected output: Error
```