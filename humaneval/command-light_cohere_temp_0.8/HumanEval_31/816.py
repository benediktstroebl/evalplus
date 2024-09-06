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
This Python function `is_prime` determines whether a given number is prime. It employs a basic heuristic of testing divisibility up to the square root of the number, using the condition `i*i <= n`. The function returns `True` if the number is prime and `False` otherwise.