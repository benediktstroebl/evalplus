Here's the solution:
```python
def x_or_y(n, x, y):
    if n % x == 0 or n % y == 0:
        return y
    else:
        return x
```

This function takes three parameters: n (which represents the number to check), x (which represents the smaller factor to check for primality), and y (which represents the larger factor to check for primality). It returns the value of x if n is a prime number and the smaller factor is not equal to y. Otherwise, it returns the factor y.