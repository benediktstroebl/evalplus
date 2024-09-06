```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and uses the **int** function to round the result of the cube root. Thus it returns true if and only if `a` is a perfect cube.