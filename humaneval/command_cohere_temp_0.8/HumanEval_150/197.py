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

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 42, 13, 13),
    (257, 19, 17, 17),
    (11, 100, -15, -15),
    (0, 99, 10, 10),
    (4, 111, 111, 111)
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    if result != expected:
        print(f"For inputs {n}, {x} and {y}, expected {expected} but got {result}")
```

The `is_prime` function is used to determine whether the number `n` is prime. If it's prime, the `x_or_y` function returns `x`; otherwise, it returns `y`. This approach allows the code to neatly separate the two behaviors and makes it easier to manage any additional logic requirements that might be added in the future.

The unit tests ensure the function performs as expected for various inputs. The `if` statements in the tests allow for some flexibility in testing additional scenarios beyond the simple "prime" and "non-prime" cases.