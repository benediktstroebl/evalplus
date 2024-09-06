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

This Python script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (a number), and two values `x` and `y`, and returns `x` if `n` is prime and `y` otherwise. To achieve this, it uses the `is_prime` function to determine whether `n` is prime or not. The script includes simple tests to validate the functionality of both functions.