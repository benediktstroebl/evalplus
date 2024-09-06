```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    import math
    if a < 0:
        a = -a
    return a ** 3 == int(math.sqrt(a ** 3))
```

This function `iscube` takes an integer number `a` as an input and returns `True` if `a` is a cube of some integer; otherwise, it returns `False`. 

The function assumes that the input is always valid, so it does not check for edge cases like `0`, `1`, or infinity.

To make the function self-contained, it uses the `math` module's `sqrt` function to calculate the square root, which is not imported in the script by default like the `int` function.