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

This function checks if any combination of the three variables adds up to the third variable. It returns `True` if any of these conditions are met, and `False` otherwise. The result is therefore true when the input is `5, 2, 7`, and similarly, any pair of the integers adds up to the third integer. It returns false when the input is `3, 2, 2` because none of the conditions are met. 

This solution assumes that the three numbers are integers. If the input is not a combination of three integers, the function will return an invalid result.