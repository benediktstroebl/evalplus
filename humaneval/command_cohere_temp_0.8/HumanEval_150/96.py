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
This code defines a function `x_or_y` that takes three arguments, `n` (the number to check for primality), `x` (the value to return if `n` is prime), and `y` (the value to return if `n` is not prime). The function uses the `is_prime` function to determine whether `n` is prime and then returns the corresponding value.

The test cases printed during the function demonstrate the behavior of the function with the provided inputs, ensuring that it returns the correct values for prime and non-prime numbers.