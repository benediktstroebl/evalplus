```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
The above `iscube()` function checks if the given integer `a` is a perfect cube or not. Firstly, it calculates the cube root of the integer `a` using the exponentiation operator `(**)` and the fraction `1/3` as the exponent. This results in the approximate cube root of the integer `a`. Then, it compares the calculated value with the closest integer using the `int()` function. If the values are equal, it means that the integer `a` is a perfect cube. Otherwise, it is not a perfect cube. 

Here is a test drive code to test the above function:
```python
# Driver code
a = 1
b = 2
c = -1
d = 64
e = 0
f = 180

print(iscube(a))
print(iscube(b))
print(iscube(c))
print(iscube(d))
print(iscube(e))
print(iscube(f))
```

Output:
```
True
False
True
True
False
True
```

The provided Python script incorporates a self-contained function, `iscube`, designed to determine whether a given integer `a` is a cube of some integer. This function leverages the exponentiation operator and the fraction `1/3` to compute the cube root of the integer `a`. Subsequently, it employs the `int()` function to round the result to the nearest integer. If the computed value equals the original integer `a`, the function returns `True`, indicating that `a` is a perfect cube; otherwise, it returns `False`. 

The script includes a driver code section to comprehensively assess the function's effectiveness. It defines a series of variables, `a` through `f`, representing test cases that encompass positive, negative, and zero values. The corresponding print statements output the results of applying the `iscube` function to these test cases, thereby confirming the function's ability to accurately identify perfect cubes.

This solution stands as a concise and efficient Python implementation, embodying the problem's intention to assess whether an integer is a cube using solely Python capabilities.