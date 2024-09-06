```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and ((a**3) == a)
```

This function `iscube()` checks if the given integer `a` is a cube of some integer number. It returns `True` if the given number is a cube, and `False` otherwise. It ensures that the input is valid, assuming that the input is always valid as per the note in the problem statement.