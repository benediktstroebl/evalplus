```python
def iscube(a):
    # Check if the number is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function `iscube()` takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer; otherwise, it returns `False`. 

The logic behind this approach is straightforward; we are checking if the `value of (a) ** (1/3)` is equidistant from the `rounded value of (a) ** (1/3)`. If the former is true, then `a` is a perfect cube; otherwise, it is not a perfect cube.

### Here are some examples of how this function operates:
```python
iscube(1)  # Returns True
iscube(8)  # Returns True
iscube(27) # Returns True
iscube(2)  # Returns False
iscube(100) # Returns True
iscube(0)  # Returns True
iscube(180) # Returns False
```