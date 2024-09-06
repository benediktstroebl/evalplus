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

This function evaluates the three conditions `a`, `b`, and `c`, each comparing one of the three input values to the sum of the other two. It then returns `True` if any of these conditions is true, and `False` otherwise.