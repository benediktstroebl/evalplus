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

This function checks if any combination of adding two of the three numbers equals the third number. 

The function returns `true` if any of these conditions are `True`, and `false` otherwise. 

It is important to note that this solution assumes that the numbers are integers. 

If the numbers were floats, a slightly different approach would be needed, for example: 

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
    d = x == y + z
    e = y == x + z
    f = z == x + y
    return bool(a or b or c or d or e or f)
```

This expanded version of the function above also checks if any of the three numbers is equal to the sum of the other two. 

And, as mentioned, this version assumes that the numbers are integers.