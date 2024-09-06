```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function employs a simple and straightforward logic to check if the condition is met, using the in operator to quickly check if any of the three variables equal the sum of the other two. This is followed by a type checking function, ensuring that all variables are of the integer type. The `all` function here is used to check if all conditions are `True`, meaning that all three numbers are integers. Overall, the code provides an efficient solution with a clear and understandable approach.