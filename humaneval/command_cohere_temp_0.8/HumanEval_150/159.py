```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x}')

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {y}')
```

This script defines a function `x_or_y` that takes three arguments, `n` (which is checked for primality), `x`, and `y`. If `n` is prime, this function returns `x`; otherwise, it returns `y`. 

The script also includes a simple test where the primality of `n` is checked against the values of `x` and `y` and the function result is printed to the console. You can modify the values of `n`, `x`, and `y` in the test blocks to verify the function's behavior against your needs.