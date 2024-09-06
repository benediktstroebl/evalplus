```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float(a)^(1/3)` is equal to an integer through the use of the `int()` function. 

This should return a True if the number is a cube, and False if it is not.