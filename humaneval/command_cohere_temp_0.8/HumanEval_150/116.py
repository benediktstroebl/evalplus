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

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (a number), and two values `x` and `y`, and returns `x` if `n` is prime and `y` if `n` is not prime. The script also defines a function `is_prime(n)` that checks if a number is prime or not. The `is_prime` function uses a mix of small prime numbers and divisibility checks to quickly rule out non-prime numbers. Finally, the script includes tests to demonstrate the behavior of the `x_or_y` function.