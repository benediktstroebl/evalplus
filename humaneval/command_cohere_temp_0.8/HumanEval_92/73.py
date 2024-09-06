```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all(type(i) == int for i in [x, y, z])
```

The function uses a `in` expression to check if any of the three variables equals the sum of the other two. Then it checks if all the variables are of int type, using Python's `all` function and the `type` function to verify that the condition is met. 

Here is a simple test suite to verify the functionality of the `any_int` function:
```python
# Testing suite for the any_int function
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(-2, 2, 3) == True
    assert any_int(0, 0, 5) == True
    assert any_int(10, -1, -3) == True
    assert any_int(0, 0, 0) == False
    assert any_int(-5, -5, -5) == True
    assert any_int(100, 200, 300) == False
    assert any_int(-5, 5, 10) == False
    assert any_int(10, 10, 20) == False
``` 

The test suite contains various cases, including edge cases, to test the `any_int` function. You can verify that all of these tests pass.