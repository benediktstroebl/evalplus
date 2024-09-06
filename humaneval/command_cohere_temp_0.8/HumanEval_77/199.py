```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float` value of `a ** (1/3)` is equal to an integer value, which would indicate that `a` is a perfect cube. 

This follows the specification of the `iscube` function, as the return value of `bool` would denote if the given value is a cube or not.