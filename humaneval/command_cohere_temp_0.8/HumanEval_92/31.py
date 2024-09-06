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
    return a or b or c
```

This function checks if any combination of the three variables adds up to the third variable. It returns `True` if any of these conditions are met, assuming that the three numbers are integers. It would return `False` if any of the numbers are not integers. 

However, this code does not validate that the numbers are integers, as the problem requires. To fix that, we can validate the inputs using assertions:
```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    assert isinstance(x, int), "x must be an integer"
    assert isinstance(y, int), "y must be an integer"
    assert isinstance(z, int), "z must be an integer"
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return a or b or c
```

With this addition, the function will return an error message if any of the inputs are not integers. 

You can test this function by calling it with different sets of arguments to verify that it returns the correct results for the given examples.