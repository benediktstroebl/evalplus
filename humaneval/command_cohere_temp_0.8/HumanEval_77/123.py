```python
def iscube(a):
    if a < 0:
        a = -a
    elif a == 0:
        return True
    while a % 3 == 0:
        a /= 3
    return a == 1
```

The function `iscube` checks if the given integer `a` is a cube of some integer. First, it handles special cases: if `a` is negative, it converts it to its absolute value by negating it; if `a` is zero, it returns `True` since zero is a cube of any number. Then, it iterates through the digits of `a` and divides `a` by 3 until the remainder becomes non-zero. Finally, it returns `True` if `a` is equal to 1, implying that it is a perfect cube. If the loop exits without a remainder of 1, it returns `False`, as it is not a perfect cube. 

This approach enables the function to efficiently determine if an integer is a cube without iterating too many divisions. It also avoids potential floating-point errors that might arise with decimal cubes and provides a precise result for valid and large test cases.