```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and uses the **int** function to round the result of the cube root. It returns True if the equation is satisfied, meaning the input is a perfect cube, and False otherwise.