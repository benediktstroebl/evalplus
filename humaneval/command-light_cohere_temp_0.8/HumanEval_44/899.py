```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    Returns string representation after base conversion.
    base numbers less 10
    base
    """
    return "{:d}".format(x, base)

# Test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(7, 2), '111')
assertEqual(change_base(10, 5), 'suits')
assertEqual(change_base(3, 1), '1337')
assertEqual(change_base(-1, 2), '-2000')
```