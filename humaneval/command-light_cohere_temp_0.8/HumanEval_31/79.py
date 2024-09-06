Here's a Python script with a self-contained function that checks if a given number is a prime:
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
This function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses some algorithm to check for primality:
- If `n <= 1`, it's not a prime
- If `n <= 3`, it's a prime
- It checks for divisibility by 2 and 3, which if the number is divisible by either, it's not prime
- Then, it checks if `n` is of the form `6k + 1`, where `k` is a prime number, by incrementing the square of a prime number by 6. 
If any of these conditions are met, it returns `False`. If none of these conditions are met, it returns `True`, indicating that `n` is a prime number.