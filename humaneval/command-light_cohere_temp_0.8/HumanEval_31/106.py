Here is a Python function that checks whether a given number is prime or not:
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
```
This function uses some basic and efficient tests to determine if a number is prime or not, including divisibility checks, square and cube multiples, and trial division up to the square root.

Note that this function is self-contained and does not require any external functions or modules to solve the problem.