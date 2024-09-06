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

The following tests show that the function any_int() behaves as expected:
```python
# True
print(any_int(5, 2, 7))
print(any_int(3, -2, 1))

# False
print(any_int(3, 2, 2))
print(any_int(3, -2, 1.2))
```

The output will be:
```bash
True
True
False
False
```