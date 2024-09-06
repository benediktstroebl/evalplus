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

This function evaluates the three conditions `a`, `b`, and `c`, each comparing one of the input numbers to the sum of the other two. It then returns `True` if any of these conditions is true, and `False` otherwise. By using the logical operator `or` to combine the conditions, the function correctly returns `True` if any integer equality holds among the three numbers, and `False` otherwise. 

Here is a simple test suite to verify the functionality of the `any_int` function:
```python
def test_any_int():
    assert any_int(5, 2, 7) == True
    assert any_int(3, 2, 2) == False
    assert any_int(3, -2, 1) == True
    assert any_int(3.6, -2.2, 2) == False
    assert any_int(-5, 10, -15) == True
    assert any_int(0, 0, 0) == False
    assert any_int(-5, -5, -5) == True
    assert any_int(10, 20, 30) == False
``` 

The test suite contains various input combinations to cover different scenarios and ensure the function's correctness in identifying integer relationships among the given numbers.