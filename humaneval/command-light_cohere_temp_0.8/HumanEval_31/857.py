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

This code defines a function `is_prime` that checks whether a given number `n` is a prime number or not. It uses the basic criteria for primality, such as the number being less than 2, less than 3, or having no perfect divisors less than or equal to the square root of the number, it then tests for each of these conditions in a loop until the condition is satisfied or `n` is greater than the square root of the number of the loop variable `i`.