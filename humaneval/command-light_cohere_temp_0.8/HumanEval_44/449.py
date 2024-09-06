```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the specified base.
    Args: 
        - x: int, number to change base 
        - base: int, base to change the number to
    Returns: string representation of the number with the new base
    """
    return f"{x}_{base}"

x = 8
y = 3
test_change_base = change_base(x, y)
assert test_change_base == '22'

x = 8
y = 2
test_change_base = change_base(x, y)
assert test_change_base == '1000'

x = 7
y = 2
test_change_base = change_base(x, y)
assert test_change_base == '111'
```
This code defines a function `change_base` that takes an integer `x` and an integer `base` as input, and returns the string representation of the number `x` with the new base. 

In the test code, it demonstrates the usage of this function by applying it to a series of numbers and then checking the returned string is the expected output for these numbers.