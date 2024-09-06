```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
```
This script defines a function `x_or_y(n, x, y)` that takes three arguments: a number `n`, and two values `x` and `y`. If `n` is prime, the function returns `x`, otherwise it returns `y`. 

To determine if a number is prime, the script also defines a helper function `is_prime(n)`. This function checks if `n` is less than 2, or if any number between 2 and the square root of `n` (inclusive) divides `n`, and returns `True` if `n` is prime, and `False` otherwise. 

Finally, the script includes a test case to demonstrate the functionality of the `x_or_y` function. 

Note that the current solution uses a simple primality testing method, which would work well for most practical purposes but is not optimized for large numbers or more sophisticated primality tests. If you need advanced primality testing, you may want to explore other primality testing libraries.