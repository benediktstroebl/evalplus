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
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. The function returns `True` if any of these conditions are true, and `False` otherwise. To achieve this, it is enough to check two of the variables as the third one can be derived from it. 

The following examples illustrate how the function works:
```python
>> any_int(5, 2, 7)
True

>> any_int(3, 2, 2)
False

>> any_int(3, -2, 1)
True

>> any_int(3.6, -2.2, 2)
False
```