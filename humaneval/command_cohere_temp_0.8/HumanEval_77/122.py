```python
def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function `iscube` takes an integer `a` as input and returns `True` if `a` is a perfect cube of an integer; otherwise, it returns `False`. 

The markdown code block describes the problem and outlines several test cases to validate the function's behavior. These test cases encompass different scenarios, including positive and negative integers, perfect cubes, and non-perfect cubes.

This code applies the cube root equation y ** 3 = x to compare `a` raised to the power of 1/3 with its rounded value. When the equation holds true and the cube root is an integer, the function returns `True`, indicating a perfect cube; otherwise, it returns `False`.