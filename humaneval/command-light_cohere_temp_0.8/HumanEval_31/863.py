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
The function checks the primality of the given number n. It first handles the the particular cases: odd numbers, numbers divisible by 2 or 3, and numbers greater than 3. If any of these are these conditions are met, the function returns False, indicating that the number is not prime; otherwise, it returns True, indicating that the number is prime.