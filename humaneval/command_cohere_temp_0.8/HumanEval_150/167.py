Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
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
print(f'x_or_y({n}, {x}, {y}) == {x}: {x_or_y(n, x, y) == x}')
n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {y}: {x_or_y(n, x, y) == y}')
```
This script includes a is_prime function that tests if a number is prime, and the x_or_y function uses this to return the correct value. The example tests are provided to demonstrate the function's behavior for different inputs.