```python
def is_prime(n):
    if n <= 1:
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
    (20, 10, 2, 2),
    (1000, 42, 2001, 2001)
]

for n, x, y, expected in tests:
    assert x_or_y(n, x, y) == expected
```

This script defines a function `x_or_y` that takes in three arguments, a number `n`, and two values `x` and `y`, and returns `x` if `n` is prime and `y` if `n` is not prime. It also defines a function `is_prime` to determine if a number is prime or not. Then, the script tests the `x_or_y` function with a list of test cases to ensure it returns the expected values for each case. 

The test cases are hard-coded in the `tests` list as a tuple of quadruples, and a loop applies the `x_or_y` function to each test case and compares the result with the expected value. 

You can add more test cases by iterating over additional tuples of quadruples and adding them to the `tests` list, and the code will handle them accordingly.