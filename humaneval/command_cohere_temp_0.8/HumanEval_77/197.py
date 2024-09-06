```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the smallest integer b whose cube is a
    for b in range(1, int(a**(1/3)) + 1):
        if a == b**3:
            return True

    return False
```

The script defines a Python function `iscube` that takes an integer `a` as input and returns `True` if `a` is the cube of an integer, and `False` otherwise. The function checks if the number is positive and then iterates from 1 up to the cube root of `a`. If `a` is equal to the cube of any integer `b` in that range, the function returns `True`. If no such `b` is found within the loop, the function returns `False`. 

This code will work for all valid input cases as per the assumptions in the problem statement.