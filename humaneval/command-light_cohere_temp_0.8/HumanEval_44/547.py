```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base b.
    If the needed conversion, return the string representation.
    Args:
        integer x (input number),
        base numbers 2 or 10.
    Returns: string representation of the number in the specified base.
    """
    return format_str(x, base)

# Test the function with different inputs and bases
x = 8
y = 3
z = 2

print(change_base(x, y))  # Expected output: 22
print(change_base(x, z))  # Expected output: 1000
print(change_base(y, z))  # Expected output: 33
print(change_base(z, y))  # Expected output: 22
```