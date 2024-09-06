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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. The function uses some algorithms to perform the primality test. It first checks if `n` is less than or equal to 1, in which case it is clearly not prime. It then checks for the other small prime numbers, checking if `n` is divisible by 2 or 3. Then, it uses the simple primality test by trying squares of primes up to the square root of `n` and checking for divisibility. If no such, it returns `True`, indicating that `n` is prime, otherwise it returns `False`. 

This code is self-contained and will correctly identify whether a given number is prime or not.