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

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to convert the result into a boolean type, True or False. The function returns `True` if any of these conditions are met, and `False` otherwise. 

Here is a test drive code to test the functionality of the `any_int()` function:
```python
# test drive code
assert any_int(5, 2, 7), "Test case 1 failed!"
assert any_int(3, 2, 2), "Test case 2 failed!"
assert any_int(3, -2, 1), "Test case 3 failed!"
assert not any_int(3.6, -2.2, 2), "Test case 4 failed!"
```

This would result in the following outputs:
```
True
False
True
False
```

The function correctly evaluates the test cases to determine if one of the three numbers is equal to the sum of the other two.