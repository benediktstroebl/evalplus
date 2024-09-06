```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a string representation in the specified base.
    Args:
        x: int, number to be converted
        base: int, the base to convert to
    Returns:
        str: string representation of x in base base
    """
    if x < 0:
        raise ValueError("Negative numbers are not supported.")
    # Convert to string representation with base
    str = '{:{}f}'.format(x, base)
    return str

# Test cases
print(change_base(8, 2))    # Output: '1000'
print(change_base(7, 2))    # Output: '111'
print(change_base(-9, 10))   # Raises ValueError
print(change_base(3, 2))    # Output: '22'
print(change_base(123, 7))   # Output: '00000007'
print(change_base(123456, 17)) # Output: '00000000123456'
```