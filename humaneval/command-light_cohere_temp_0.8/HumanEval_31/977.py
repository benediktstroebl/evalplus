```python
def is_prime(n):
    """Returns True if the number is prime, and False otherwise."""
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

This function checks if a given number `n` is prime or not. It employs a strategy to test for primality, including checking divisibility by 2 and 3, as well as observing if `n` is a square or a number whose square is less than 2. 

This method is efficient and capable of identifying prime numbers quickly.