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
    """Return x if n is a prime number, otherwise return y."""
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

The `is_prime` function checks if a number is prime using a standard algorithm. The `x_or_y` function uses `is_prime` to determine whether to return `x` or `y`. The last two lines are examples of tests that can be used to check the correctness of the `x_or_y` function. 

This solution is relatively simple and straightforward, but it correctly solves the problem and passes the provided tests.  It does not handle the edge case of when `n` is `0` or `1`, neither does it address the case of `x` and `y` being equal, both of which are trivial to do and can be included as warranted by the problem statement.  It also doesn't abuse any logical nuances for performance optimization, opting instead for a straightforward boolean check. 

This script can be easily adapted to include other cases that may need to be considered.