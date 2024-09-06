```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are string must be a decimal number or a power of 10 (e.
    """
    example: change_base(8, 3) returns '22', which is 22 in base 3
    """
    # Convert x to a string in the desired base
    return ''.join` _((x * power(base, x)) if isinstance(x, int) and x >= 0 else '?n' * 'inf')
    # where power(base, x) returns a power of 10 raised to the given number
    # Convert to integer again
    return int(x)

def test():
    x = 8
    base = 3
    assert change_base(x, base) == '22'
    x = 8
    base = 2
    assert change_base(x, base) == '1000'
    x = 7
    base = 2
    assert change_base(x, base) == '111'

# Run the test function to check the function's correctness
test()
```