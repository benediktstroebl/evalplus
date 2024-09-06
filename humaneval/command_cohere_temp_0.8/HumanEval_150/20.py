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

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (16, 42, 7, 7),
    (27, 13, 17, 13),
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    assert result == expected, f"For inputs {n}, {x} , {y} expected {expected} but got {result}"
```

The `is_prime` function is introduced to provide a more understandable and reusable factorization utility. It works by checking if a number is less than 2, or if it has any divisors other than 1 and itself up to the square root of the number. Any number that passes these tests is considered prime. 

The `x_or_y` function then uses `is_prime` to determine whether to return `x` or `y`.