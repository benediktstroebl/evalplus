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
This code defines a function called is_prime that takes an integer n as input and returns true if n is a prime number, and false otherwise. The function implements a popular Sieve of Eratosthenes algorithm to check for primality, iteratively eliminating the multiples of numbers starting from 2 and 3 up to the target number.