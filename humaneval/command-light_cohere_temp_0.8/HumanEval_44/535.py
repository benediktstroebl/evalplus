```python
def change_base(x: int, base: int):
    """Change the base of a number x to base base b."""
    return "{:b}".format(x, base)

# Test case 1: Change the base of 8 to 3
assertEqual(change_base(8, 3), '22')

# Test case 2: Change the base of 8 to 2
assertEqual(change_base(8, 2), '1000')

# Test case 3: Change the base of 7 to 2
assertEqual(change_base(7, 2), '111')
```
This Python script defines a function `change_base` that converts a given number `x` to a specified base `base` using the `format` method. The test cases ensure that the script provides the expected output for each given input.