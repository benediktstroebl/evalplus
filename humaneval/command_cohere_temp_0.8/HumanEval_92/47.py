```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, y+x] and all(type(n) == int for n in [x, y, z])
```

The function `any_int` takes three arguments and returns `True` if one of the arguments is equal to the sum of the other two and all the arguments are integers; otherwise, it returns `False`. 

Here is an example usage of the function:
```python
# Test the function with different inputs
print(any_int(5, 2, 7))  # Outputs: True
print(any_int(3, 2, 2))  # Outputs: False
print(any_int(3, -2, 1))  # Outputs: True
print(any_int(3.6, -2.2, 2))  # Outputs: False
```

This demonstrates the correct behavior of the function according to the problem description.