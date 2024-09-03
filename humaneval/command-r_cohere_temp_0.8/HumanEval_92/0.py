```python
def any_int(x, y, z):
    '''
    Checks if one number is the sum of the other two and all numbers are integers.
    
    Parameters:
    x (int): A number.
    y (int): A number.
    z (int): A number.
    
    Returns:
    bool: True if one number is the sum of the other two, and all numbers are integers, otherwise False.
    '''
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    
    s = x + y
    return s == z or s == x or s == y
```