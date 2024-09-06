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

This function checks if any combination of adding two of the three numbers equals the third number. The function returns true if a combination exists, and false if none exist. Given that the numbers must be integers, this condition would not be fulfilled for floats. 

The function returns a boolean value that corresponds to the truthfulness of the statement 'any two of the numbers equal the third number'. 

The `bool()` function converts the expression to a boolean value, which returns either `True` or `False`. 

This approach allows for a simple and efficient way of solving the problem, without requiring complex computations.