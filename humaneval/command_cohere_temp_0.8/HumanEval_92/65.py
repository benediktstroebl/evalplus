```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all(type(i) == int for i in [x, y, z])
```

The problem asks the function to return true if one of the numbers is equal to the sum of the other two and the three numbers are integers. The code uses the in operator to check if any of the variables equals the sum of the other two and the type function, to verify if all the variables are of int type. Both arguments and locally defined functions in Python have their own docstrings that can be documented accordingly.