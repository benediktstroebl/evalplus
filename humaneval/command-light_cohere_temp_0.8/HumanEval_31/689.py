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
This Python function `is_prime` accepts an integer `n` as input and outputs a boolean indicating whether `n` is a prime number or not. The function implements a various rules to determine if a number is prime or not, and the output is True if all the tests pass and False otherwise.