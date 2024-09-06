```python
def iscube(a):
    # Check if the number is greater than 0 and equals to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number given is greater than 0, then it checks if the `float` value of `a` raised to the power of `1/3` is an integer with the int() function. If it is an integer, it returns True since the input is assumed to be valid, greater than zero, and equal to the cube of some integer. Otherwise, it returns False. This algorithm is case-insensitive, so it would return True for -27, and 270. 

This problem can be solved more efficiently with the use of `math.ceil` and `math.sqrt`. Below is an optimized version of the previous code:
```python
def iscube(a):
    # Check if the number is greater than 0 and equals to the cube of some integer
    return a > 0 and int(math.ceil(math.sqrt(a ** (1/3)))) ** 3 == a
```

This version calculates the cube of the integer that is the ceiling of the square root of a **(1/3)**th power. It is more efficient as it avoids calculating the fractional part of the `a ** (1/3)` result. 

To achieve this, it is important to know that a perfect cube is the number formed by multiplying an integer by itself three times. Recognizing the symmetry of this problem allows us to find the solution more efficiently.