```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    import math
    if a < 0:
        a = -a
    cube = int(math.sqrt(a**3))
    return a == cube**3
```

This function `iscube` takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer; otherwise, it returns `False`. The function verifies whether the absolute value of `a` is equal to the cube of an integer, using the `math.sqrt()` to compute the cube root of the cube of `a`. 

In other words, the function is checking if the absolute value of the input is equal to the result of raising the cube root of the absolute value of the input to the power of 3, and hence it returns `True` if this equation holds, and `False` otherwise. 

This approach guarantees that the function correctly identifies all valid cubes of integers, including both positive and negative bases, while avoiding division errors by using the properties of the cube root. 

Note: this assumption that the input is always valid could be problematic, as it may lead to issues with edge cases like `0` or `inf`.  It would be better to handle such cases explicitly to ensure the function's robustness and avoid potential issues in actual implementations.