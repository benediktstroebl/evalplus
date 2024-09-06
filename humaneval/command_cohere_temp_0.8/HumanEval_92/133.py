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

The function returns `True` if any of these conditions are met, indicating that at least one of the given numbers is equal to the sum of the other two numbers. 

The function returns `False` if none of these conditions are met, indicating that all of the numbers are different from each other. 

Feel free to test this function with different inputs to verify its behavior.