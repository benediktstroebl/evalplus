```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Parameters:
        x: int or float
            Input number to convert
        base: int
            Base to convert from or to convert to
    Returns:
        str: The string representation of x in the specified base
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if not isinstance(base, int):
        raise TypeError("Base must be an integer")

    # Implementation:
    base = base % 10  # Ensure base is a single-digit decimal digit
    ret = ""
    while x > 0:
        digit = x % base
        ret = str(digit) + ret
        x //= base
    return ret

# Unit tests
test_change_base = []
test_change_base.push( (123, 10))
test_change_base.push((5_b, 10)
test_change_base.push((5.5, 10)
test_change_base.push((7, 10) )
test_change_base.push((23, 100)
test_change_base.push((5, 10) )
test_change_base.push((45, 10)

def test_function():
    test_change_base

# Execution
```