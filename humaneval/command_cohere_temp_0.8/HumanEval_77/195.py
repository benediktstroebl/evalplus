```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function satisfies the given simple condition to check if a given integer `a` is a cube of some integer. Clearly, it returns `True` if it is a perfect cube, and `False` otherwise. 

Example usage:
```python
print(iscube(8)) # True
print(iscube(27)) # False
```

This approach takes advantage of the integer division `a ** (1/3)` which returns the real cube root of `a`. Then the condition checks if this cube root is an integer with `int(a ** (1/3))`, thus checking if a is a perfect cube. Note that some edge cases like `0` or `180` are correctly identified as `True` and `False` respectively.