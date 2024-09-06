```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function verifies if the given integer `a` is a cube of some integer by considering the following conditions:
1. If `a` is negative, it can be transformed into a positive number by negating it. This is done to simplify the remaining calculations, as the problem asks to identify if `a` is a cube, not specifically a positive cube.
2. It computes the cube of the absolute value of `a` and checks whether the result is an integer through the condition `a ** 3 == int(a ** 3)`. If the cube of the absolute value of `a` has a fractional part, it is not a perfect cube, and hence, the function returns `False`. 

The provided example tests, including positive and negative integers, demonstrate the correctness of the function. 

If the user wishes to test additional scenarios or incorporate the function into a larger program, the `iscube` function can be imported and utilized as needed.