```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a given number x to the specified base.
    Args:
        x: The number to be converted
        base: The base to which the number will be converted
    Returns:
        string representation of the converted number
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input values")
    result = ''
    while x > 0:
        digit = x % base
        result = str(digit) + result
        x //= base
    return result

# Example usage:
x = 8
base = 2
try:
    print(change_base(x, base))
except ValueError as e:
    print(f"Error: {e}")
```