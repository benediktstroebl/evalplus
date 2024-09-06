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
This function checks whether a given number is prime or not. It uses the shallow testing to check divisibility by 2, 3, and then iteratively larger primes up to the square root of the number. It also checks for larger prime numbers using an optimized sqrt(n) loop.