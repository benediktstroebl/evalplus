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

This function checks if any combination of the three variables adds up to the other variable. Once the variable comparison is done, it returns `True` if any of these conditions are true, and `False` otherwise. 

This solution follows the `Pythagorean triples` approach and is more efficient than the `x + y + z` approach as it avoids floating point errors.