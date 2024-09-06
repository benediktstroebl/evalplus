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

This function checks if any combination of adding two of the three numbers equals the third number. The result is True if any of these conditions are true, and False otherwise. Here is an example usage of the function:
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
This matches the desired behavior of the provided examples.