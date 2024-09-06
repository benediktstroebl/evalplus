Here is a self-contained Python script that defines a function is_prime(n) that checks whether a given number is a prime:
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

This function is_prime checks various conditions for primality, such as divisibility by 2 and 3, divisibility by consecutive primes up to the square root of the number, and checking for divisibility by larger primes. The function ultimately returns True if the is prime and False otherwise.