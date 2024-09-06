```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    Returns string representation after base conversion.
    """
    string representation after conversion
    """
    if x < 0 or base < 2 or base > 36:
        raise ValueError("Invalid input.
    if base == 10 and x < 0:
        return str(x)
    else:
        return format(x, base)
    return "Error: invalid input"

# Test cases
print(change_base(-8, 3))     # Should print '22'
print(change_base(0, 2))    # Should print '1000'
print(change_base(5, 8))    # Should print '55'
print(change_base(2, 10))  # Should print '20'
print(change_base(-5, 2))  # Should print 'Error'
print(change_base(123, 1)) # Should print 'Error'
print(change_base(10, 5))  # Should print 'Error'

```