```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base base.
    Returns the string representation of the number using the new base.
    """
    string representation after conversion from the original base.
    """
    raised ValueError: base cannot be negative"""
    if base < 0:
        raise ValueError("base cannot be negative")
    return "{x}".format(str(base))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(-3, 10))  # Raises ValueError as base is negative
print(change_base(123, -2))  # Raises ValueError as base is negative
```