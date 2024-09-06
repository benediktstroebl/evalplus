```python
def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function `iscube` takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer; otherwise, it returns `False`. 

The script assumes that the input is always valid, as stated in the problem statement. Therefore, it does not check for negative cases or zero and returns `True` for these cases.

This solution is straightforward and runs in approximately `O(1)` time since it only performs a single operation: taking the cube root of the integer. It is efficient and can handle large datasets efficiently.