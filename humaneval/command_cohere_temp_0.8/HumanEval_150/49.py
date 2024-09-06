```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (101, -5, 5, 5),
    (0, 10, 11, 11),
    (4, 2, 3, 3),
    (2, 20, 19, 19),
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    assert result == expected, f"For inputs {n}, {x} and {y}, expected {expected} but got {result}"
```

The `is_prime` function is used to determine whether the given number n is prime. The `x_or_y` function then returns the value of x if n is prime, and y otherwise. Finally, the script tests the function with a variety of cases to ensure it matches the expected behavior.