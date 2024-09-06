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

This function checks if any combination of the three variables adds up to the other variable. Once the variables are compared, the function returns `True` if any of the conditions are met, and `False` otherwise.

This problem can also be solved in other ways, such as using `any()` and `all()` functions like this: 
```python
def any_int(x, y, z):
    return any((x == y + z, y == x + z, z == x + y)) and all(isinstance(n, int) for n in (x, y, z))
```

Which approach do you prefer for this problem? Let me know if you want me to explain any of the approaches in greater depth!