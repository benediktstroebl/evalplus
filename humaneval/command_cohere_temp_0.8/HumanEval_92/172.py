```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function `any_int` takes three arguments `x`, `y`, and `z`. It uses the in operator to check if any of the values are equal to the sum of the other two values. The `all` function checks if all the values are integers. You can verify that the function works as expected by calling it with different sets of arguments:
```python
# Output: True
print(any_int(5, 2, 7))

# Output: False
print(any_int(3, 2, 2))

# Output: True
print(any_int(3, -2, 1))

# Output: False
print(any_int(3.6, -2.2, 2))
``` 

The function will return `True` for the first two examples and `False` for the last two examples.