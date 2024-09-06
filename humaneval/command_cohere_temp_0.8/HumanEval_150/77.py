```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')  # Output: True

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')  # Output: True
```

This code defines a function `x_or_y` that takes three arguments: `n` (which is assumed to be either a prime number or a non-prime number), `x` (which should be returned if `n` is prime), and `y` (which should be returned if `n` is not prime). The function uses the `is_prime` function to determine whether `n` is prime or not. If it's prime, `x` is returned; otherwise, `y` is returned.

The script then provides two examples that illustrate the behavior of the `x_or_y` function.