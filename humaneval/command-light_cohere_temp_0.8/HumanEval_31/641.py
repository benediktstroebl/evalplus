```python
def is_prime(n):
    """
    Returns true if the number is prime, and false otherwise.
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
This function uses trial division and checks divisibility conditions to determine if a number is prime. The function returns True if the number is prime, and False otherwise.