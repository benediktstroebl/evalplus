```python
def is_prime(n):
    """
    Returns True if the number is prime, False otherwise.
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
This code defines a function named is_prime that checks whether a given number is prime or not. The function starts by handling special cases where the number is less than or equal to 1, as these are definitely not prime. Then, it checks for numbers less than or equal to 3, as they are prime. Next, it performs a Miller-Rabin primality test, which is a more efficient test for primality. It iterates a value of i, and checks if n is divisible by i or i + 2. If it fails, it returns False, indicating that n is not prime. If all these tests fail, it returns True, indicating that n is prime.