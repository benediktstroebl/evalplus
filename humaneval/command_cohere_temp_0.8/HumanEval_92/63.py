```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all(type(n) == int for n in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the in operator to check if any of the values are equal to the sum of the other two values. The `all` function with a generator expression is used to check if all the values are integers. The generator expression `type(n) == int for n in [x, y, z]` checks if all types of the three arguments are integer types.