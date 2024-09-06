```python
def change_base(x: int, base: int):
    """
    Convert number to desired base representation.
    """
    base numbers under 10
    > change_base(8, 2)
    '1000'
    > change_base(7, 2)
    '111'
    """
    return '{:0>d}'.format(x, base)

# Unit tests
print(change_base(8, 2))      # Output: 1000
print(change_base(7, 2))      # Output: 111
print(change_base(15, 10))    # Output: 22
print(change_base(123, 2))   # Output: 00000022
print(change_base(5, 10))    # Output: 0522
```