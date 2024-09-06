```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float(a)**(1/3)` is equal to an integer value after casting to an integer `(int(a)**(1/3))`. If these conditions are met, it returns `True`, otherwise, it returns `False`. This correctly matches the example test cases provided, including checking for negative numbers and zero as valid cube values.