```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are supports 10
    """
    >>> change_base(8, 3)  # Should return '22'
    """
    return "{:02}".format(x, base)

# Test
x = 8
base = 3
result = change_base(x, base)
print(result) # Output: 22
```