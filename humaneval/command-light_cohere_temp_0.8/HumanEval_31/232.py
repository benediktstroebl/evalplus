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
This code defines a function called is_prime that checks whether a given number is prime or not. It uses a first phase to filter out the numbers with a factor less than or equal to 2 or 3, then uses a trial and error approach with the help of the square root property to find any possible factors and check if the number is prime or not.