Here's a self-contained Python function to check if a number is prime:
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
This function uses a simple algorithm to check if a number is prime, and passes all the tests provided. It starts by checking numbers less than 2 and 3, then uses a simple looping structure to try divisibility up to the square root of the number. It returns true if no divisors are found after the loop completes.