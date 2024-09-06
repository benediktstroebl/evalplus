```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number is greater than zero, which guarantees there is always a cube root. After this condition is checked, the function proceeds to evaluate `a ** (1/3)`, obtaining the floating-point result of the cube root. The function then converts this result to the nearest integer using the `int()` function and checks if this integer is equal to the original input. If these conditions are met, the function returns `True`, otherwise, it returns `False`. 

This algorithm has a time complexity of `O(1)` since it involves simple arithmetic operations and comparisons.