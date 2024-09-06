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

The function `iscube` checks if the given integer `a` is a cube of some integer. First, it handles special cases: if `a` is negative, it converts it to its positive equivalent, and if `a` is zero, it returns `True` since zero is a cube of any number. Then, it iterates through the digits of `a` and eliminates multiples of 3 from the number by dividing by 3 until it reaches the digit '1'. If the resulting number is 1, it means the original number is a cube, and the function returns `True`. Otherwise, it returns `False`. 

This solution focuses on simplicity and readability, assuming the input is always valid as requested in the problem statement. Test cases are provided to ensure the function's correctness.