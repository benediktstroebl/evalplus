```python
def change_base(x: int, base: int):
    """
    Changes the base of a number x to the specified base.
    :return string representation after conversion.
    """
    string literals are converted using int()
    """
    return f"{x:d}".format(format_='{base}')

x = 8
test_change_base = lambda base: str(change_base(x, base)) == '22'
test_change_base(10) # Should return True
test_change_base(2) # Should return True
test_change_base(42) # Should return False
```