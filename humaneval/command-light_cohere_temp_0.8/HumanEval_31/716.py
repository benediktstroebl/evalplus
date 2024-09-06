Here's a Python script with a self-contained function that solves the problem of checking if a number is prime, and passes the corresponding tests:
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

This function, `is_prime()`, uses a basic algorithm to check for primality. It first handles simple base case of numbers less than or equal to 1. Then, it checks for the multiple divisors of the number, starting from 2 and 3 (since they are both prime numbers). The algorithm then iterates up to the square of the current number, doubling the threshold for checking divisors. Finally, if the number has no divisors or has only one divisor within the doubled threshold, it is considered prime.