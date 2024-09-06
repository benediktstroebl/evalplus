```python
def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))
```

This function simplifies the problem by directly checking if the integer can be cubed to yield the original value. It also ignores the decimal value of the answer. For example, iscube(2) returns False because 2 is not a perfect cube, even though 2^(1/3) is approximately 1.25996. The function rounds this value to 1, so it would return True. Finally, the function handles fractional inputs by comparing the fractional part to 0.5 using the expression `x ** (1/3) == round(x ** (1/3))`, which will return True if the fractional part is 0.5 or -0.5. 

However, if you want to be able to distinguish between -1 and 1, modify the function to make the rounding more precise:
```python
def iscube(a):
    # Check if the integer a is a perfect cube
    third = a ** (1/3)
    return round(third, 3) == third
```

This will return False for -1, because the value of (-1) ** (1/3) is NaN, and when rounded to 3 decimal places, it becomes NaN. It will also return False for 2, because 2 ** (1/3) is approximately 1.1547, and when rounded to 3 decimal places, it becomes 1.152.