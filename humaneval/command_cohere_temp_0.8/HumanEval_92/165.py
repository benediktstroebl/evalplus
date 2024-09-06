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
    return a or b or c
```

The function will return True if at least one of the conditions is True, indicating that one of the numbers is equal to the sum of the other two. 

Here is a test suite that can be used to validate the functionality of the code:
```python
def test_any_int():
    # True case
    assert any_int(5, 2, 7) == True
    assert any_int(3, -2, 1) == True

    # False case
    assert any_int(3, 2, 2) == False
    assert any_int(3.6, -2.2, 2) == False

test_any_int()
```

This would ensure that the function behaves as expected and follows the specifications provided.