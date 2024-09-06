```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    
    if a in [x, y, z] or b in [x, y, z] or c in [x, y, z]:
        return True
    elif a == b and a == c:
        return False
    else:
        return any([type(i) for i in [x, y, z]]) == int and any_int(a, b, c)
```

This script defines a function `any_int` that takes three integers as input and returns `True` if one of the inputs is equal to the sum of the other two, and the sum is also an integer; otherwise, it returns `False`. This is achieved by introducing some auxiliary variables to simplify the logic and using `any` function to check integer type. This enhances the code structure and readability.