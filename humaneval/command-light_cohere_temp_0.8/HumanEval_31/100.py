Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
This code defines a function is_prime that checks whether a given number n is a prime number or not. It starts by considering numbers up to 3, then checks for divisibility by 2 and 3, and subsequently uses a iterative 'while i*i <= n' condition to check for divisibility up to sqrt(n) which means checking up to the square root of n. This is method ensures the uniqueness of prime numbers and handles numbers greater than 3.