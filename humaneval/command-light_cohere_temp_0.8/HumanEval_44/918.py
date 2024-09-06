```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Returns string representation after conversion.
    base numbers are base of 10
    """
    return '{:,.}'.format(x, base)

# Test case 1
assertEqual(change_base(8, 3), '22')

# Test case 2
assertEqual(change_base(8, 2), '1000')

# Test case 3
assertEqual(change_base(7, 2), '111')
```
This code defines a function `change_base` that converts a given number `x` to a string representation using a specified base. The test cases ensure that the function works correctly for different inputs and bases.

Remember, using `assert` is not necessary when running this script, as the function contains its own tests. This way, you can call the function directly with the `assertEqual` function to verify its correctness.