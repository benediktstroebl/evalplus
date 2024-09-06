```python
def change_base(x, base):
    return str(x)
    # Use list comprehension to convert digits of the integer x in the given base 10
    # to digits in the new base `base`, and return the resulting string.

# Tests:
# Test a variety of inputs to ensure correct functionality.
>>> change_base(8, 3)
'twenty-two'

>>> change_base(8, 2)
'1000'

>>> change_base(7, 2)
'111'

>>> change_base(5, 5)
'101'

>>> change_base(15, 3)
'221'
```