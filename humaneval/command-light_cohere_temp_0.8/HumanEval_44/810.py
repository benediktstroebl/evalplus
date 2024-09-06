```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    return '{:0{}b}'.format(x, base)

# Test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(8, 2), '1000')
assertEqual(change_base(7, 2), '111')
assertEqual(change_base(10, 10), '101010')
assertEqual(change_base(10, 5), '5')
assertEqual(change_base(10, 3), '110')
assertEqual(change_base(10, 2), '20')
assertEqual(change_base(10, 4), '200')
assertEqual(change_base(10, 6), '164')
assertEqual(change_base(10, 7), '1710')
assertEqual(change_base(10, 8), '180')
assertEqual(change_base(10, 9), '18')
```
This Python script defines a function `change_base` that converts a given number `x` to a string representation in the specified base. It uses f-string formatting to achieve this, which is a built-in function in Python strings. This function is tests various cases with different inputs and bases, and the output is compared against the expected results using the `assertEqual` function.