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

This function checks if any combination of adding two of the three numbers equals the third number. The result is True if any equality is found, otherwise, it is False. The function returns True when the given example values are used, and it also returns False when the additional example values are used. 

Here is a simple test suite that can be used to validate the function:
```python
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

test_any_int()
``` 
The `test_any_int` test case will execute the `any_int` function with the inputs provided in the MD block, and it will assert if the output matches the expected True or False values.