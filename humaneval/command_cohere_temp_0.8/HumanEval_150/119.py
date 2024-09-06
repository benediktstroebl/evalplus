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

This script utilizes a fundamental approach to prime checking by iterating from 2 to `n`'s square root and looking for divisors. The `x_or_y` function uses this helper function to determine whether to return `x` or `y`. The test cases are also included to validate the function against the problem statement. Adjust the values of `n`, `x`, and `y` in the test cells as needed.