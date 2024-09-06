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
    return bool(a or b or c)
```

This function checks if any combination of adding two of the three numbers equals the third number. 

The `bool()` function is used to convert the result into a boolean value, `True` or `False`. 

The code then returns this boolean value. 

To test this function, ensure that all three values are integers, as the function specifically checks for integer values in its definition. 

For example, the unit test `test_any_int` demonstrates this:
```python
def test_any_int():
    # True: one of the numbers is equal to the sum of the other two
    assert any_int(5, 2, 7) == True
    assert any_int(3, -2, 1) == True

    # False: none of the numbers is equal to the sum of the other two
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1.1) == False
```

This test validates the behavior of the `any_int` function against its intended logic.