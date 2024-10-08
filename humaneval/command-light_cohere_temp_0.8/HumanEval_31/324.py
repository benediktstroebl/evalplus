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
The function `is_prime` checks if a given number is prime or not, it returns True if the number is prime and False otherwise. It uses a simple optimization to test for divisibility by 2 and 3, then uses a loop to check divisibility up to the square root of the number, if the number is divisible by any number less than or equal to the square root, then it is a prime number.