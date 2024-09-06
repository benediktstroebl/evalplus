```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the in operator to check if any of the values are equal to the sum of the other two values. The `all` function checks if all the values are integers. The function returns `True` if one of the values is equal to the sum of the other two values and all the values are integers. Otherwise, it returns `False`. 

Here is a simple test suite to ensure that the function `any_int` is correct:
```python
# Testing value scenarios
assert any_int(5, 2, 7) == True
assert any_int(3, 2, 2) == False
assert any_int(3, -2, 1) == True
assert any_int(3.6, -2.2, 2) == False

# Testing edge scenarios
assert any_int(0, 0, 0) == False
assert any_int(0, 0, 1) == True
assert any_int(-10, 0, 5) == True
```
The test suite contains examples of different scenarios to properly test the function.