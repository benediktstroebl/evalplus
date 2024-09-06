```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to convert the result into a boolean type.

Here are some examples of this function in use:
```python
TestSuite = [(any_int(5, 2, 7), True),
             (any_int(3, 2, 2), False),
             (any_int(3, -2, 1), True),
             (any_int(3.6, -2.2, 2), False)]
```

The expected result is provided in the corresponding cell.