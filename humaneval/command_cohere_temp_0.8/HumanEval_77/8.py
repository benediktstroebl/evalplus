```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `float(a)^(1/3)` is equal to an integer value after casting to int. It returns True if these conditions are both satisfied and `False` otherwise. 

This problem can be solved more elegantly with the use of symmetries, but the above implementation follows the most straightforward approach and should be sufficiently optimized for test cases that are symmetric across cubing, rounding, and equality constraints.