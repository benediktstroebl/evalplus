```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    import math
    if a < 0:
        a = -a
    s := math.sqrt(a)
    return s * s * s == a
```

This function `iscube` takes an integer number `a` as an input and returns `True` if `a` is a cube of some integer; otherwise, it returns `False`. The function uses a math module to assert the cube condition `s * s * s == a`. 

The function's logic is based on the following conditions:
- If `a` is a perfect cube, it will return `True`.
- If `a` is negative, it will ignore the negative, check if the absolute value of `a` is a cube, and return `True`.
- If `a` is zero, it will return `True`.
- If `a` is not a perfect cube and is not zero, it will return `False`.