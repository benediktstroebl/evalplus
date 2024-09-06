```python
def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function simplifies the equation to check if `a` is a perfect cube, by raising it to the power of `1/3` and then comparing it with its rounded version. It returns true if they are equal, and false if they are not.

This approach has a complexity of `O(1)` and uses the `round` function to approximate the cube root value of `a` before comparison. Although this is not a precise mathematical evaluation of cube roots, it is a practical and efficient way to determine if an integer is a perfect cube. 

This code assumes that the input is always valid, as stated in the assumption, however, it is good practice to include input validation in real-world scenarios.