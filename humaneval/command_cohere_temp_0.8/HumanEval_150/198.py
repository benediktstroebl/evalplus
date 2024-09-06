```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
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
    (2, 42, 10, 10),
    (17, 89, 13, 13)
]

for n, x, y, expected in tests:
    actual = x_or_y(n, x, y)
    if actual != expected:
        print(f"For inputs {n}, {x} and {y}, expected {expected} but got {actual}")
        exit(1)
```

This code defines a function `x_or_y` that takes three arguments (`n`, `x`, and `y`) and returns `x` if the former is a prime number and `y` otherwise. 

To do this, the function calls `is_prime`, a helper function also included in the code, which determines whether a given number is prime or not. It does this by iterating from 2 to the square root of `n`, checking if any numbers in that range divide `n` without leaving a remainder, and therefore not prime. 

The code also includes a list of tests that verify the function against examples from the problem statement, and exits with an error code if any of the tests fail. 

This code can be run directly to test it. However, to make testing easier, it's generally a good idea to incorporate this code into a larger testing framework, such as a module in a Python project. This can help ensure that each test is executed in isolation and any failures are more clearly identified.