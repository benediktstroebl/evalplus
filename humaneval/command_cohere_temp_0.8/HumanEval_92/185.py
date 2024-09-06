```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return any([a, b, c])
```

This function checks if any combination of adding two of the three numbers equals the third number. Then the function returns `true` if any of these conditions are `True`, otherwise it returns `false`. 

Here is a test suite that could be used to test this function:
```python
# Testing suite for the any_int function
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False

    assert any_int(-5, -1, 0) == True
    assert any_int(-5, 1, 0) == False
    assert any_int(-5, -2, -1) == True
    assert any_int(-5, -2, 1) == False  

test_any_int()
```
This testing suite contains multiple test functions that test the `any_int` function with different cases. Each test function name starts with the word `test_`, which is a convention that lets the Python interpreter know that these functions are test functions. 

The `assert` statement is used to check if the first expression evaluates to `True` in the context of the second expression. If the first expression evaluates to `False` the Python interpreter will throw an error and the test will fail. If the first expression evaluates to `True` the test will pass.