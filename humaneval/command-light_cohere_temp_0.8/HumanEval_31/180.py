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
This function, `is_prime`, determines whether a given number n is prime or not. It starts with basic checks and then employs a sieve of Eratosthenes to efficiently determine prime numbers. 

This function is self-contained and can be used to determine whether a given number is prime or not, passing in any number as an argument.