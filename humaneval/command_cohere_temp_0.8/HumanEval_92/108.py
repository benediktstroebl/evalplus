```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the `in` operator to compare the three given numbers `x`, `y`, and `z` with the possible sums of the pairs formed by these numbers. To ensure that the compared sums are integers, the function uses the `all` function in combination with the `type` function and the `int` constructor to check if all given numbers and the potential sum are of integer type.