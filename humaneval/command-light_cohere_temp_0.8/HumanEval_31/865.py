Here is a self-contained Python script that defines a function to determine if a given number is a prime, passing all the test cases provided:

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
```

This function uses a series of conditions and divisibility checks to determine if a given number is prime or not. The function returns true if the prime and false otherwise. The function handles numbers that are greater than 2.

This solution is self-contained and doesn't rely on external functions or modules. It provides a straight and clear implementation of the given problem.