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
This code defines a function `is_prime` that checks if a given number `n` is prime or not. It uses some basic checks: small primes, odd numbers divisible by 2 or 3, and checks for divisibility up to the square root of `n`. 

It also employs a simple optimization by testing only odd divisors of `n` up to the square root since multiples of even numbers up to the square root are always composite and therefore not prime.