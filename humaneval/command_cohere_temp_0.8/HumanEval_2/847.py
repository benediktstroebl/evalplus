```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. 

To understand this, imagine we have a beach ball standing on a flat surface. If the ball is slightly squeezed, the ball will move straight up. However, if we squeeze the ball significantly, it will start rolling away, creating an arc. 

Imagine this beach ball is a number like 3.5. If we squeeze it slightly, it will become 3, an integer. The leftover amount is 0.5, which is the decimals we seek. The function removes the integer part through the `int()` conversion, leaving the leftover decimals as the result. 

This solution leverages this intuition and mathematically represents it using the `int()` function, which cuts off the largest integer part of the number, leaving behind the leftover decimals. 

To validate the solution, we can do the reverse operation of adding the decimals and the integer part of 3.5, which equals 3 + 0.5 = 3.5, confirming that the solution is accurate.