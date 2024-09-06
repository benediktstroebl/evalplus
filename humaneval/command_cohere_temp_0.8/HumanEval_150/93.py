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
    (20, 10, 2, 2),
    (unteared, 10, 2, 2),
    (4, 10, 2, 2),
    (100, 10, 2, 2),
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    assert result == expected, f"For inputs {n}, {x} and {y}, expected {expected} but got {result}"
``` 

This script defines a function `x_or_y` that takes three arguments `n` (the number to check), `x` (the value to return if `n` is prime), and `y` (the value to return otherwise). The function uses the `is_prime` function to determine whether `n` is prime and returns `x` or `y` accordingly.

The unit tests are then defined and used to check the function with different inputs and ensure that the function returns the expected value for each test case.  This is a simple and efficient approach to solve this problem and pass the given tests.  If you have any questions, let me know!