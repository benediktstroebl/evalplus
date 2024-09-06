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
This function, `is_prime`, evaluates whether a given number is a prime or not. It starts by checking numbers less than or equal to 2 and 3, since they are prime. It then uses a prime numbers checking algorithms like the Sieve of Eratosthenes, Legendreux, or trial division, to efficiently determine if the number is prime or not.