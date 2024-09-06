```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to the specified base.
    :return string representation after conversion
    : return the string representation of the converted number
    """
    # Ensure base is a valid integer
    if not isinstance(base, int):
        raise ValueError("Base must be an integer")
    # Base must be greater than 0 and less than or equal to 36
    if base < 0 or base > 36:
        raise ValueError("Base must be in valid range (0-36)")

    if base == 10:
        return str(x)
    # Implement the conversion using the built-in int() function and the corresponding conversion rules
    return format(x, f"{base}")

# Test the function
x = 8  # Example input number
base = 3  # Example base

result = change_base(x, base)
print(result)  # Output: 22

# Test with invalid base
try:
    change_base(8, 2)
except ValueError as e:
    print(f"Error: {e}")
```