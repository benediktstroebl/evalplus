```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    Args:
        x: int, the number to be converted
        base: int, base to convert to.aya: int base to convert the
    Returns:
        str representation in the specified base
    """
    return '{:02}'.format(x, base)

# Test the function
test_case = [8, 3]
test_output = change_base(*test_case)
assert test_output == '22'
test_case = [8, 2]
test_output = change_base(*test_case)
assert test_output == '1000'
test_case = [7, 2]
test_output = change_base(*test_case)
assert test_output == '111'
```
This code defines a function called `change_base` that takes two arguments: `x` and `base`. The function then returns a string representation of `x` in the specified base `base`.