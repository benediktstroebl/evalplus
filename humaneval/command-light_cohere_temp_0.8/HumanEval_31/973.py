```python
def is_prime(n):
    """ Returns True if n is prime, False otherwise.
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
This function, is_prime, checks whether a given number n is prime or not. It uses the basic sieve algorithm to find all prime numbers up to n. The function then returns True if n is prime and False otherwise.