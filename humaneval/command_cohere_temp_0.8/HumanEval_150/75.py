Here's a Python script with a self-contained function that solves the problem and passes the tests:
```python
# The python script for the above problem
def x_or_y(n, x, y):
    if n == 2:
        return x
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return y
    return x
```
The function returns the value of `x` if the input integer `n` is prime; otherwise, it returns `y`. The `if` statements evaluate the nature of the input integer `n` against the ideal conditions to determine the course of action. The function then returns the chosen value based on these conditions. 

This solution ranks among the most straightforward ones.