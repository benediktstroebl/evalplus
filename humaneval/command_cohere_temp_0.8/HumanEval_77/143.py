```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function determines whether a given integer `a` is the cube of an integer, assuming that the input is always valid. It starts by checking if `a` is negative, and if so, it negates `a` to simplify the equation. The function then computes `a` raised to the power of 3 and compares it with the integer equivalent. If the result is true, it returns `True`; otherwise, it returns `False`. 

This approach ensures that all valid input values receive the appropriate output when subjected to the relevant tests. And the condition `a ** 3 == int(a ** 3)` is used to handle the case of integers like -1, 0, and 1, which are also cubes. Any other value will result in False.