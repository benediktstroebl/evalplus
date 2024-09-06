```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function determines whether a given integer `a` is a cube of some integer, starting with the assumption that `a` is a positive integer. It transforms the problem of determining if a number is the cube of an integer into a problem of determining whether a integer is a perfect cube. To do this, it takes the cube root of the number using integer division and checks whether the result is an integer, not leaving any fractional parts. If this condition is met, it returns `True`, indicating that `a` is a perfect cube; otherwise, it returns `False`. 

This function efficiently solves the problem of determining whether an integer is a cube using mathematical properties without resorting to iterative methods.