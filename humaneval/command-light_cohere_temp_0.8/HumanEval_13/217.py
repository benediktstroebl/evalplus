Here's a self-contained Python function that finds the greatest common divisor of two integers:
```python
def greatest_common_divisor(a, b):
    if not_dividend(a) and not_dividend(b):
        return a
    elif not_multiply(a) and not_multiply(b):
        return b
    else:
        return gcd(a, b)

def not_dividend(x):
    return not x == 0

def not_multiply(x):
    return not x == 1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
```
This script defines the function `greatest_common_divisor`, which accepts two integers `a` and `b` as arguments. The function employs the specific cases for the existence of common divisors and employs the `gcd` function to compute the greatest common divisor. 

Please note that this code is self-contained and effectively solves the problem.