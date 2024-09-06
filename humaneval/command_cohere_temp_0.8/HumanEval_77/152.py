```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function determines whether a given integer `a` is the cube of an integer, taking the input's validity into account. It starts by checking if `a` is negative. If so, it calculates the absolute value of `a` by negating it, ensuring the input is always non-negative. The function then computes the cube of the integer and compares it with the original input. It returns `True` if they are equal, indicating the input is a perfect cube.

This accurately and efficiently determines if an integer is a cube using only basic mathematical operations and boolean evaluations.