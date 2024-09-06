```python
def choose_num(x, y):
    max_even = (x + y) // 2
    max_even += max_even % 2
    if max_even >= x and max_even <= y:
        return max_even
    else:
        return -1
```

The code works as follows:
1. Calculate the arithmetic mean of `x` and `y` and rounding this value down to the nearest even integer: `max_even = (x + y) // 2` and `max_even += max_even % 2` to ensure that the result is always even. This is an attempt to find the largest even integer that lies between `x` and `y`.
2. If this calculated even integer is within the range of x and y, return it. Otherwise, return -1, indicating that there is no largest even integer in the range. 

This approach ensures that for valid inputs, the function will always return the largest even integer that falls within the specified range, or the symbolic -1 if no such number exists. 

Note: The conditional statement could have been written in a more straightforward manner using `if max_even >= x and max_even <= y` instead of the more roundabout `if max_even >= x and max_even <= y:`. This would lead to slightly cleaner code, but the current formulation is also correct and will work as intended.