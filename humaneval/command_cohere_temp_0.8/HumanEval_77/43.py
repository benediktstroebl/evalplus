```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function simply computes the cube root of the number and checks if the result is an integer. The `int()` function ensures that the result is rounded down, so the condition is true when the cube root is an integer.